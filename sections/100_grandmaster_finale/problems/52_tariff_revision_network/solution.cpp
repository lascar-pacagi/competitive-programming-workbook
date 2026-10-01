#include <bits/stdc++.h>
using namespace std;

// Offline dynamic MST by divide and conquer over the update timeline.
// At a node covering updates [l, r], the edges modified inside the range are
// "dynamic"; every other edge has a fixed weight throughout the range.
//   * Contraction: static edges chosen by Kruskal even when all dynamic edges
//     are forced first belong to every MST of the range -> contract them.
//   * Reduction: static edges rejected by Kruskal on static edges alone can
//     never enter an MST of the range -> delete them.
// After both steps a node with k dynamic edges keeps O(k) vertices and edges.

struct Edge {
    int u, v, id;
};

int n, m, q;
vector<long long> weight;
vector<int> qe;
vector<long long> qw;
vector<int> dynamicStamp;
vector<long long> answers;

struct DSU {
    vector<int> parent;
    void reset(int size) {
        parent.resize(size);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int x) {
        while (parent[x] != x) x = parent[x] = parent[parent[x]];
        return x;
    }
    bool unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        parent[a] = b;
        return true;
    }
};

void solve(int l, int r, int vertices, vector<Edge> edges, long long base) {
    auto byWeight = [](const Edge& a, const Edge& b) {
        return weight[a.id] < weight[b.id];
    };
    if (l == r) {
        weight[qe[l]] = qw[l];
        sort(edges.begin(), edges.end(), byWeight);
        DSU dsu;
        dsu.reset(vertices);
        long long total = base;
        for (const Edge& e : edges)
            if (dsu.unite(e.u, e.v)) total += weight[e.id];
        answers[l] = total;
        return;
    }
    static int stampCounter = 0;
    int stamp = ++stampCounter;
    for (int i = l; i <= r; i++) dynamicStamp[qe[i]] = stamp;

    vector<Edge> dyn, stat;
    for (const Edge& e : edges)
        (dynamicStamp[e.id] == stamp ? dyn : stat).push_back(e);
    sort(stat.begin(), stat.end(), byWeight);

    // Contraction.
    DSU dsu;
    dsu.reset(vertices);
    for (const Edge& e : dyn) dsu.unite(e.u, e.v);
    DSU forced;
    forced.reset(vertices);
    for (const Edge& e : stat)
        if (dsu.unite(e.u, e.v)) {
            forced.unite(e.u, e.v);
            base += weight[e.id];
        }
    vector<int> label(vertices, -1);
    int newVertices = 0;
    for (int v = 0; v < vertices; v++) {
        int root = forced.find(v);
        if (label[root] < 0) label[root] = newVertices++;
        label[v] = label[root];
    }

    // Reduction on the contracted graph.
    dsu.reset(newVertices);
    vector<Edge> next;
    next.reserve(dyn.size() * 2 + 1);
    for (const Edge& e : stat) {
        int a = label[e.u], b = label[e.v];
        if (a != b && dsu.unite(a, b)) next.push_back({a, b, e.id});
    }
    for (const Edge& e : dyn) next.push_back({label[e.u], label[e.v], e.id});

    int mid = (l + r) / 2;
    solve(l, mid, newVertices, next, base);
    solve(mid + 1, r, newVertices, next, base);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n >> m >> q;
    weight.resize(m);
    vector<Edge> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].u >> edges[i].v >> weight[i];
        edges[i].u--;
        edges[i].v--;
        edges[i].id = i;
    }
    qe.resize(q);
    qw.resize(q);
    for (int i = 0; i < q; i++) {
        cin >> qe[i] >> qw[i];
        qe[i]--;
    }
    dynamicStamp.assign(m, 0);
    answers.resize(q);
    solve(0, q - 1, n, edges, 0);
    string out;
    for (long long x : answers) out += to_string(x) + '\n';
    cout << out;
}
