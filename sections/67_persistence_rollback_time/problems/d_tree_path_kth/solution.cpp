#include <bits/stdc++.h>
using namespace std;

struct Node {
    int left = 0;
    int right = 0;
    int count = 0;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;
    vector<int> value(n), compressed;
    for (int& x : value) cin >> x;
    compressed = value;
    sort(compressed.begin(), compressed.end());
    compressed.erase(unique(compressed.begin(), compressed.end()),
                     compressed.end());

    vector<vector<int>> graph(n);
    for (int edge = 1; edge < n; ++edge) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int levels = bit_width(static_cast<unsigned>(n));
    vector<vector<int>> up(levels, vector<int>(n));
    vector<int> depth(n), order = {0};
    for (int index = 0; index < n; ++index) {
        int u = order[index];
        for (int v : graph[u]) {
            if (v == up[0][u] || v == 0) continue;
            up[0][v] = u;
            depth[v] = depth[u] + 1;
            order.push_back(v);
        }
    }
    for (int level = 1; level < levels; ++level) {
        for (int u = 0; u < n; ++u) {
            up[level][u] = up[level - 1][up[level - 1][u]];
        }
    }

    vector<Node> tree(1);
    auto insert = [&](auto&& self, int old, int low, int high,
                      int position) -> int {
        int current = static_cast<int>(tree.size());
        tree.push_back(tree[old]);
        ++tree[current].count;
        if (low != high) {
            int middle = (low + high) / 2;
            if (position <= middle) {
                tree[current].left = self(self, tree[old].left, low, middle,
                                          position);
            } else {
                tree[current].right = self(self, tree[old].right, middle + 1,
                                           high, position);
            }
        }
        return current;
    };

    vector<int> root(n);
    for (int u : order) {
        int rank = lower_bound(compressed.begin(), compressed.end(), value[u])
                   - compressed.begin();
        int parent_root = (u == 0 ? 0 : root[up[0][u]]);
        root[u] = insert(insert, parent_root, 0,
                         static_cast<int>(compressed.size()) - 1, rank);
    }

    auto lca = [&](int u, int v) {
        if (depth[u] < depth[v]) swap(u, v);
        int difference = depth[u] - depth[v];
        for (int level = 0; level < levels; ++level) {
            if (difference >> level & 1) u = up[level][u];
        }
        if (u == v) return u;
        for (int level = levels - 1; level >= 0; --level) {
            if (up[level][u] != up[level][v]) {
                u = up[level][u];
                v = up[level][v];
            }
        }
        return up[0][u];
    };

    auto kth = [&](int a, int b, int c, int d, int k) {
        int low = 0;
        int high = static_cast<int>(compressed.size()) - 1;
        while (low != high) {
            int left_count = tree[tree[a].left].count
                           + tree[tree[b].left].count
                           - tree[tree[c].left].count
                           - tree[tree[d].left].count;
            int middle = (low + high) / 2;
            if (k <= left_count) {
                a = tree[a].left;
                b = tree[b].left;
                c = tree[c].left;
                d = tree[d].left;
                high = middle;
            } else {
                k -= left_count;
                a = tree[a].right;
                b = tree[b].right;
                c = tree[c].right;
                d = tree[d].right;
                low = middle + 1;
            }
        }
        return low;
    };

    while (q--) {
        int u, v, k;
        cin >> u >> v >> k;
        --u;
        --v;
        int ancestor = lca(u, v);
        int before = (ancestor == 0 ? 0 : root[up[0][ancestor]]);
        int rank = kth(root[u], root[v], root[ancestor], before, k);
        cout << compressed[rank] << '\n';
    }
}
