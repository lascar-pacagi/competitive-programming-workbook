#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> parent, size;
    DSU(int n) : parent(n), size(n, 1) { iota(parent.begin(), parent.end(), 0); }
    int find(int u) { return parent[u] == u ? u : parent[u] = find(parent[u]); }
    void join(int u, int v) {
        u = find(u); v = find(v);
        if (u == v) return;
        if (size[u] < size[v]) swap(u, v);
        parent[v] = u; size[u] += size[v];
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;
    vector<pair<int, int>> edges(m);
    for (auto &[u, v] : edges) { cin >> u >> v; --u; --v; }
    struct Operation { char type; int x, y; };
    vector<Operation> operations(q);
    vector<char> deleted(m);
    for (auto &[type, x, y] : operations) {
        cin >> type >> x; --x;
        if (type == 'D') { y = -1; deleted[x] = true; }
        else { cin >> y; --y; }
    }
    DSU dsu(n);
    for (int e = 0; e < m; ++e)
        if (!deleted[e]) dsu.join(edges[e].first, edges[e].second);
    vector<string> answers;
    for (int i = q - 1; i >= 0; --i) {
        auto [type, x, y] = operations[i];
        if (type == 'D') dsu.join(edges[x].first, edges[x].second);
        else answers.push_back(dsu.find(x) == dsu.find(y) ? "YES" : "NO");
    }
    reverse(answers.begin(), answers.end());
    for (const string &answer : answers) cout << answer << '\n';
}
