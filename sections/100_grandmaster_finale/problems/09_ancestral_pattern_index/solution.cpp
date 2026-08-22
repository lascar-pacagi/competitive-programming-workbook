#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

constexpr int MOD1 = 1'000'000'007;
constexpr int MOD2 = 1'000'000'009;
constexpr int BASE = 911382323;

struct Segment {
    int left, right;
    bool reversed;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    string labels;
    cin >> n >> q >> labels;
    vector<vector<int>> graph(n);
    for (int i = 1; i < n; ++i) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<int> parent(n, -1), depth(n), order{0};
    for (size_t at = 0; at < order.size(); ++at) {
        int u = order[at];
        for (int v : graph[u]) {
            if (v == parent[u]) continue;
            parent[v] = u;
            depth[v] = depth[u] + 1;
            order.push_back(v);
        }
    }
    vector<int> size(n, 1), heavy(n, -1);
    for (int at = n - 1; at > 0; --at) {
        int u = order[at], p = parent[u];
        size[p] += size[u];
        if (heavy[p] == -1 || size[u] > size[heavy[p]]) heavy[p] = u;
    }
    vector<int> head(n), position(n), vertex_at(n);
    vector<pair<int, int>> tasks{{0, 0}};
    int timer = 0;
    while (!tasks.empty()) {
        auto [start, chain_head] = tasks.back();
        tasks.pop_back();
        for (int u = start; u != -1; u = heavy[u]) {
            head[u] = chain_head;
            position[u] = timer;
            vertex_at[timer++] = u;
            for (int v : graph[u])
                if (parent[v] == u && v != heavy[u]) tasks.push_back({v, v});
        }
    }

    auto lca = [&](int u, int v) {
        while (head[u] != head[v]) {
            if (depth[head[u]] > depth[head[v]]) u = parent[head[u]];
            else v = parent[head[v]];
        }
        return depth[u] < depth[v] ? u : v;
    };
    auto path_segments = [&](int u, int v) {
        int ancestor = lca(u, v);
        vector<Segment> result, down;
        while (head[u] != head[ancestor]) {
            result.push_back({position[head[u]], position[u] + 1, true});
            u = parent[head[u]];
        }
        result.push_back({position[ancestor], position[u] + 1, true});
        while (head[v] != head[ancestor]) {
            down.push_back({position[head[v]], position[v] + 1, false});
            v = parent[head[v]];
        }
        if (position[ancestor] + 1 <= position[v])
            down.push_back({position[ancestor] + 1, position[v] + 1, false});
        reverse(down.begin(), down.end());
        result.insert(result.end(), down.begin(), down.end());
        return result;
    };

    vector<int> base(n), reversed_base(n);
    for (int i = 0; i < n; ++i) base[i] = labels[vertex_at[i]] - 'a' + 1;
    for (int i = 0; i < n; ++i) reversed_base[i] = base[n - 1 - i];
    array<vector<int>, 2> powers, prefix, reverse_prefix;
    int moduli[2] = {MOD1, MOD2};
    for (int h = 0; h < 2; ++h) {
        int mod = moduli[h];
        powers[h].resize(n + 1, 1);
        prefix[h].resize(n + 1);
        reverse_prefix[h].resize(n + 1);
        for (int i = 0; i < n; ++i) {
            powers[h][i + 1] = static_cast<int64>(powers[h][i]) * BASE % mod;
            prefix[h][i + 1] = (static_cast<int64>(prefix[h][i]) * BASE + base[i]) % mod;
            reverse_prefix[h][i + 1] =
                (static_cast<int64>(reverse_prefix[h][i]) * BASE + reversed_base[i]) % mod;
        }
    }
    auto range_hash = [&](const array<vector<int>, 2> &source, int left, int right) {
        int parts[2];
        for (int h = 0; h < 2; ++h) {
            int mod = moduli[h];
            parts[h] = (source[h][right]
                - static_cast<int64>(source[h][left]) * powers[h][right - left] % mod
                + mod) % mod;
        }
        return pair{parts[0], parts[1]};
    };
    auto segment_hash = [&](const Segment &segment, int offset, int length) {
        if (!segment.reversed)
            return range_hash(prefix, segment.left + offset,
                              segment.left + offset + length);
        int original_left = segment.right - offset - length;
        int original_right = segment.right - offset;
        return range_hash(reverse_prefix, n - original_right, n - original_left);
    };
    auto segment_character = [&](const Segment &segment, int offset) {
        int base_position = segment.reversed ? segment.right - 1 - offset
                                             : segment.left + offset;
        return base[base_position];
    };

    while (q--) {
        int u, v, x, y;
        cin >> u >> v >> x >> y;
        --u; --v; --x; --y;
        vector<Segment> first = path_segments(u, v);
        vector<Segment> second = path_segments(x, y);
        int i = 0, j = 0, offset_first = 0, offset_second = 0, common = 0;
        int comparison = 0;
        while (i < static_cast<int>(first.size()) &&
               j < static_cast<int>(second.size())) {
            int remaining_first = first[i].right - first[i].left - offset_first;
            int remaining_second = second[j].right - second[j].left - offset_second;
            int take = min(remaining_first, remaining_second);
            if (segment_hash(first[i], offset_first, take) ==
                segment_hash(second[j], offset_second, take)) {
                common += take;
                offset_first += take;
                offset_second += take;
                if (offset_first == first[i].right - first[i].left) {
                    ++i;
                    offset_first = 0;
                }
                if (offset_second == second[j].right - second[j].left) {
                    ++j;
                    offset_second = 0;
                }
                continue;
            }
            int low = 0, high = take;
            while (low < high) {
                int middle = (low + high + 1) / 2;
                if (segment_hash(first[i], offset_first, middle) ==
                    segment_hash(second[j], offset_second, middle)) low = middle;
                else high = middle - 1;
            }
            common += low;
            int a = segment_character(first[i], offset_first + low);
            int b = segment_character(second[j], offset_second + low);
            comparison = a < b ? -1 : 1;
            break;
        }
        if (comparison == 0) {
            bool first_finished = i == static_cast<int>(first.size());
            bool second_finished = j == static_cast<int>(second.size());
            if (first_finished != second_finished) comparison = first_finished ? -1 : 1;
        }
        cout << common << ' ' << comparison << '\n';
    }
}
