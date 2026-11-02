#include <bits/stdc++.h>
using namespace std;

#include <algorithm>
#include <cassert>
#include <queue>
#include <vector>

struct Dinic {
    struct Edge {
        int to;
        long long cap;
    };
    int n;
    std::vector<Edge> edges;
    std::vector<std::vector<int>> adj;
    std::vector<int> level, ptr;

    explicit Dinic(int n) : n(n), adj(n) {}

    int add_edge(int u, int v, long long capacity) {
        assert(0 <= u && u < n && 0 <= v && v < n);
        assert(capacity >= 0);
        int edge = static_cast<int>(edges.size());
        adj[u].push_back(edge);
        edges.push_back({v, capacity});
        adj[v].push_back(edge ^ 1);
        edges.push_back({u, 0});
        return edge;
    }

    bool bfs(int s, int t) {
        level.assign(n, -1);
        level[s] = 0;
        std::queue<int> queue;
        queue.push(s);
        while (!queue.empty()) {
            int u = queue.front();
            queue.pop();
            for (int edge : adj[u]) {
                int v = edges[edge].to;
                if (edges[edge].cap > 0 && level[v] == -1) {
                    level[v] = level[u] + 1;
                    queue.push(v);
                }
            }
        }
        return level[t] != -1;
    }

    long long send(int s, int t, long long limit) {
        std::vector<int> vertices{s}, path;
        std::vector<long long> bottleneck{limit};
        while (!vertices.empty()) {
            int u = vertices.back();
            if (u == t) {
                long long delta = bottleneck.back();
                for (int edge : path) {
                    edges[edge].cap -= delta;
                    edges[edge ^ 1].cap += delta;
                }
                return delta;
            }
            while (ptr[u] < static_cast<int>(adj[u].size())) {
                int edge = adj[u][ptr[u]];
                int v = edges[edge].to;
                if (edges[edge].cap > 0 && level[v] == level[u] + 1)
                    break;
                ++ptr[u];
            }
            if (ptr[u] == static_cast<int>(adj[u].size())) {
                vertices.pop_back();
                bottleneck.pop_back();
                if (!path.empty()) {
                    path.pop_back();
                    ++ptr[vertices.back()];
                }
            } else {
                int edge = adj[u][ptr[u]];
                path.push_back(edge);
                vertices.push_back(edges[edge].to);
                bottleneck.push_back(
                    std::min(bottleneck.back(), edges[edge].cap));
            }
        }
        return 0;
    }

    long long max_flow(int s, int t) {
        assert(0 <= s && s < n && 0 <= t && t < n && s != t);
        long long added = 0, limit = 0;
        for (int edge : adj[s]) limit += edges[edge].cap;
        while (bfs(s, t)) {
            ptr.assign(n, 0);
            while (long long delta = send(s, t, limit)) added += delta;
        }
        return added;
    }

    std::vector<bool> reachable(int s) const {
        std::vector<bool> seen(n, false);
        seen[s] = true;
        std::queue<int> queue;
        queue.push(s);
        while (!queue.empty()) {
            int u = queue.front();
            queue.pop();
            for (int edge : adj[u]) {
                int v = edges[edge].to;
                if (edges[edge].cap > 0 && !seen[v]) {
                    seen[v] = true;
                    queue.push(v);
                }
            }
        }
        return seen;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, k, q;
    if (!(cin >> n >> m >> k >> q)) return 0;
    vector<long long> cost(n);
    long long budget = 0;
    for (auto& x : cost) { cin >> x; if (x >= 0) budget += x; }
    vector<int> starts(k), targets(q);
    vector<bool> protected_room(n);
    for (int& v : starts) { cin >> v; --v; protected_room[v] = true; }
    for (int& v : targets) { cin >> v; --v; protected_room[v] = true; }
    long long inf = budget + 1;
    int s = 2 * n, t = s + 1;
    Dinic flow(t + 1);
    for (int v = 0; v < n; ++v) {
        long long c = cost[v] < 0 || protected_room[v] ? inf : cost[v];
        flow.add_edge(2 * v, 2 * v + 1, c);
    }
    for (int v : starts) flow.add_edge(s, 2 * v, inf);
    for (int v : targets) flow.add_edge(2 * v + 1, t, inf);
    while (m--) {
        int u, v; cin >> u >> v;
        flow.add_edge(2 * (u - 1) + 1, 2 * (v - 1), inf);
    }
    long long answer = flow.max_flow(s, t);
    cout << (answer >= inf ? -1 : answer) << '\n';
}
