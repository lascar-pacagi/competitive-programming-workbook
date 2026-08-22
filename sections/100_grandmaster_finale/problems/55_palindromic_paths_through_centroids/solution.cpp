#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

constexpr int MOD = 998244353;
constexpr int ROOT = 3;

int mod_power(int base, int exponent) {
    int64 result = 1;
    while (exponent) {
        if (exponent & 1) result = result * base % MOD;
        base = static_cast<int64>(base) * base % MOD;
        exponent >>= 1;
    }
    return result;
}

void ntt(vector<int> &a, bool inverse) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; ++i) {
        int bit = n >> 1;
        while (j & bit) {
            j ^= bit;
            bit >>= 1;
        }
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    for (int length = 2; length <= n; length <<= 1) {
        int step = mod_power(ROOT, (MOD - 1) / length);
        if (inverse) step = mod_power(step, MOD - 2);
        for (int start = 0; start < n; start += length) {
            int64 root = 1;
            for (int offset = 0; offset < length / 2; ++offset) {
                int u = a[start + offset];
                int v = root * a[start + offset + length / 2] % MOD;
                a[start + offset] = u + v;
                if (a[start + offset] >= MOD) a[start + offset] -= MOD;
                a[start + offset + length / 2] = u - v;
                if (a[start + offset + length / 2] < 0)
                    a[start + offset + length / 2] += MOD;
                root = root * step % MOD;
            }
        }
    }
    if (inverse) {
        int inverse_n = mod_power(n, MOD - 2);
        for (int &x : a) x = static_cast<int64>(x) * inverse_n % MOD;
    }
}

vector<int> convolution(const vector<int> &a, const vector<int> &b) {
    if (a.empty() || b.empty()) return {};
    int total = a.size() + b.size() - 1;
    if (min(a.size(), b.size()) < 40) {
        vector<int> result(total);
        for (int i = 0; i < static_cast<int>(a.size()); ++i)
            for (int j = 0; j < static_cast<int>(b.size()); ++j)
                result[i + j] = (result[i + j]
                    + static_cast<int64>(a[i]) * b[j]) % MOD;
        return result;
    }
    int size = 1;
    while (size < total) size <<= 1;
    vector<int> first(a.begin(), a.end()), second(b.begin(), b.end());
    first.resize(size);
    second.resize(size);
    ntt(first, false);
    ntt(second, false);
    for (int i = 0; i < size; ++i)
        first[i] = static_cast<int64>(first[i]) * second[i] % MOD;
    ntt(first, true);
    first.resize(total);
    return first;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> color(n);
    for (int &c : color) cin >> c;
    vector<vector<int>> graph(n);
    for (int i = 1; i < n; ++i) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<bool> blocked(n);
    vector<int> parent(n), subtree_size(n), answer(n);

    auto find_centroid = [&](int start) {
        vector<int> nodes{start};
        parent[start] = -1;
        for (size_t at = 0; at < nodes.size(); ++at) {
            int u = nodes[at];
            for (int v : graph[u]) {
                if (blocked[v] || v == parent[u]) continue;
                parent[v] = u;
                nodes.push_back(v);
            }
        }
        for (auto it = nodes.rbegin(); it != nodes.rend(); ++it) {
            int u = *it;
            subtree_size[u] = 1;
            for (int v : graph[u])
                if (!blocked[v] && parent[v] == u)
                    subtree_size[u] += subtree_size[v];
        }
        int total = nodes.size();
        int centroid = start, best = total + 1;
        for (int u : nodes) {
            int largest = total - subtree_size[u];
            for (int v : graph[u])
                if (!blocked[v] && parent[v] == u)
                    largest = max(largest, subtree_size[v]);
            if (largest < best) {
                best = largest;
                centroid = u;
            }
        }
        return centroid;
    };

    auto add_square = [&](const vector<int> &polynomial, int sign) {
        vector<int> product = convolution(polynomial, polynomial);
        int limit = min(n, static_cast<int>(product.size()));
        for (int distance = 0; distance < limit; ++distance) {
            answer[distance] += sign * product[distance];
            if (answer[distance] >= MOD) answer[distance] -= MOD;
            if (answer[distance] < 0) answer[distance] += MOD;
        }
    };

    auto decompose = [&](auto &&self, int start) -> void {
        int centroid = find_centroid(start);
        array<vector<int>, 2> all;
        all[color[centroid]].resize(1, 1);

        for (int neighbor : graph[centroid]) {
            if (blocked[neighbor]) continue;
            array<vector<int>, 2> branch;
            vector<tuple<int, int, int>> stack{{neighbor, centroid, 1}};
            while (!stack.empty()) {
                auto [u, p, distance] = stack.back();
                stack.pop_back();
                if (static_cast<int>(branch[color[u]].size()) <= distance)
                    branch[color[u]].resize(distance + 1);
                ++branch[color[u]][distance];
                for (int v : graph[u])
                    if (!blocked[v] && v != p)
                        stack.push_back({v, u, distance + 1});
            }
            for (int c = 0; c < 2; ++c) {
                add_square(branch[c], -1);
                if (all[c].size() < branch[c].size()) all[c].resize(branch[c].size());
                for (int d = 0; d < static_cast<int>(branch[c].size()); ++d) {
                    all[c][d] += branch[c][d];
                    if (all[c][d] >= MOD) all[c][d] -= MOD;
                }
            }
        }
        add_square(all[0], 1);
        add_square(all[1], 1);
        blocked[centroid] = true;
        for (int neighbor : graph[centroid])
            if (!blocked[neighbor]) self(self, neighbor);
    };

    decompose(decompose, 0);
    answer[0] = 0;
    int inverse_two = (MOD + 1) / 2;
    for (int distance = 1; distance < n; ++distance)
        answer[distance] = static_cast<int64>(answer[distance]) * inverse_two % MOD;
    for (int distance = 0; distance < n; ++distance)
        cout << answer[distance] << " \n"[distance + 1 == n];
}
