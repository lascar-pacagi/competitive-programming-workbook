#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> parent, sz;
    DSU(int n) : parent(n), sz(n, 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }
    bool unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (sz[a] < sz[b]) swap(a, b);
        parent[b] = a;
        sz[a] += sz[b];
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<tuple<long long, int, int>> edges;
    for (int i = 0; i < m; i++) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        edges.push_back({w, u - 1, v - 1});
    }
    sort(edges.begin(), edges.end());
    DSU dsu(n);
    long long total = 0;
    int used = 0;
    for (auto [w, u, v] : edges) {
        if (dsu.unite(u, v)) {
            total += w;
            used++;
        }
    }
    if (used != n - 1) cout << "IMPOSSIBLE\n";
    else cout << total << '\n';
    return 0;
}

