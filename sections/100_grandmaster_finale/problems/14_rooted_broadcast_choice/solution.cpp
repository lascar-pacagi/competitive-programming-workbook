#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int from, to;
    long long cost;
};

long long directed_mst(int vertices, int root, vector<Edge> edges) {
    const long long INF = (1LL << 62);
    long long answer = 0;
    while (true) {
        vector<long long> incoming(vertices, INF);
        vector<int> parent(vertices, -1);
        for (const auto &edge : edges) {
            if (edge.from != edge.to && edge.cost < incoming[edge.to]) {
                incoming[edge.to] = edge.cost;
                parent[edge.to] = edge.from;
            }
        }
        incoming[root] = 0;
        for (int v = 0; v < vertices; ++v) {
            if (incoming[v] == INF) return -1;
            answer += incoming[v];
        }

        int cycles = 0;
        vector<int> component(vertices, -1), seen(vertices, -1);
        for (int start = 0; start < vertices; ++start) {
            int v = start;
            while (seen[v] != start && component[v] == -1 && v != root) {
                seen[v] = start;
                v = parent[v];
            }
            if (v != root && component[v] == -1) {
                for (int u = parent[v]; u != v; u = parent[u]) {
                    component[u] = cycles;
                }
                component[v] = cycles++;
            }
        }
        if (cycles == 0) return answer;

        for (int v = 0; v < vertices; ++v) {
            if (component[v] == -1) component[v] = cycles++;
        }
        vector<Edge> contracted;
        contracted.reserve(edges.size());
        for (const auto &edge : edges) {
            int from = component[edge.from];
            int to = component[edge.to];
            long long cost = edge.cost;
            if (from != to) cost -= incoming[edge.to];
            contracted.push_back({from, to, cost});
        }
        root = component[root];
        vertices = cycles;
        edges.swap(contracted);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<long long> activation(n);
    for (long long &cost : activation) cin >> cost;

    const long long PENALTY = (long long)(n + 1) * 1'000'000'000LL + 1;
    vector<Edge> edges;
    edges.reserve(m + n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long cost;
        cin >> u >> v >> cost;
        edges.push_back({u - 1, v - 1, cost});
    }
    int super_root = n;
    for (int v = 0; v < n; ++v) {
        edges.push_back({super_root, v, PENALTY + activation[v]});
    }

    long long encoded = directed_mst(n + 1, super_root, edges);
    if (encoded < 0 || encoded / PENALTY != 1) cout << -1 << '\n';
    else cout << encoded % PENALTY << '\n';
}
