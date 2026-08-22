#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long sum = 0;
    int left = 0;
    int right = 0;
    int count = 0;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;
    vector<long long> value(n), coordinates;
    for (long long &x : value) cin >> x;
    coordinates = value;
    sort(coordinates.begin(), coordinates.end());
    coordinates.erase(unique(coordinates.begin(), coordinates.end()), coordinates.end());

    vector<vector<int>> graph(n);
    for (int i = 1; i < n; ++i) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int log = 1;
    while ((1 << log) <= n) ++log;
    vector<vector<int>> up(log, vector<int>(n));
    vector<int> depth(n), order{0};
    up[0][0] = 0;
    for (size_t at = 0; at < order.size(); ++at) {
        int u = order[at];
        for (int v : graph[u]) {
            if (v == up[0][u] && u != 0) continue;
            up[0][v] = u;
            depth[v] = depth[u] + 1;
            order.push_back(v);
        }
    }
    for (int bit = 1; bit < log; ++bit)
        for (int v = 0; v < n; ++v)
            up[bit][v] = up[bit - 1][up[bit - 1][v]];

    auto lca = [&](int u, int v) {
        if (depth[u] < depth[v]) swap(u, v);
        int difference = depth[u] - depth[v];
        for (int bit = 0; bit < log; ++bit)
            if (difference >> bit & 1) u = up[bit][u];
        if (u == v) return u;
        for (int bit = log - 1; bit >= 0; --bit) {
            if (up[bit][u] != up[bit][v]) {
                u = up[bit][u];
                v = up[bit][v];
            }
        }
        return up[0][u];
    };

    vector<Node> tree(1);
    tree.reserve(static_cast<size_t>(n) * (log + 2));
    auto insert = [&](auto &&self, int previous, int left, int right,
                      int position, long long x) -> int {
        int current = static_cast<int>(tree.size());
        tree.push_back(tree[previous]);
        ++tree[current].count;
        tree[current].sum += x;
        if (right - left == 1) return current;
        int middle = (left + right) / 2;
        if (position < middle)
            tree[current].left = self(self, tree[previous].left, left, middle,
                                      position, x);
        else
            tree[current].right = self(self, tree[previous].right, middle, right,
                                       position, x);
        return current;
    };

    vector<int> root(n);
    for (int v : order) {
        int previous = v == 0 ? 0 : root[up[0][v]];
        int position = lower_bound(coordinates.begin(), coordinates.end(), value[v])
                     - coordinates.begin();
        root[v] = insert(insert, previous, 0, coordinates.size(), position, value[v]);
    }

    auto combined_count = [&](int a, int b, int c, int d) {
        return tree[a].count + tree[b].count - tree[c].count - tree[d].count;
    };
    auto combined_sum = [&](int a, int b, int c, int d) {
        return tree[a].sum + tree[b].sum - tree[c].sum - tree[d].sum;
    };

    while (q--) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        int ancestor = lca(u, v);
        int before = ancestor == 0 ? 0 : root[up[0][ancestor]];
        int a = root[u], b = root[v], c = root[ancestor], d = before;
        int length = combined_count(a, b, c, d);
        long long total = combined_sum(a, b, c, d);
        int wanted = (length + 1) / 2;
        int left = 0, right = coordinates.size();
        long long lower_sum = 0;
        int lower_count = 0;

        while (right - left > 1) {
            int al = tree[a].left, bl = tree[b].left;
            int cl = tree[c].left, dl = tree[d].left;
            int count_left = combined_count(al, bl, cl, dl);
            int middle = (left + right) / 2;
            if (wanted <= count_left) {
                a = al;
                b = bl;
                c = cl;
                d = dl;
                right = middle;
            } else {
                wanted -= count_left;
                lower_count += count_left;
                lower_sum += combined_sum(al, bl, cl, dl);
                a = tree[a].right;
                b = tree[b].right;
                c = tree[c].right;
                d = tree[d].right;
                left = middle;
            }
        }
        lower_count += combined_count(a, b, c, d);
        lower_sum += combined_sum(a, b, c, d);
        long long median = coordinates[left];
        long long cost = median * lower_count - lower_sum
                       + (total - lower_sum) - median * (length - lower_count);
        cout << median << ' ' << cost << '\n';
    }
}
