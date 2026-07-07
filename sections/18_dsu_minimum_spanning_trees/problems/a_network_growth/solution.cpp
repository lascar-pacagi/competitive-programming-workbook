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
    int unite(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return sz[ra];
        if (sz[ra] < sz[rb]) swap(ra, rb);
        parent[rb] = ra;
        sz[ra] += sz[rb];
        return sz[ra];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    DSU dsu(n);
    int components = n, largest = 1;
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        if (dsu.find(u) != dsu.find(v)) {
            largest = max(largest, dsu.unite(u, v));
            components--;
        }
        cout << components << ' ' << largest << '\n';
    }
    return 0;
}

