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
    int n, p;
    if (!(cin >> n >> p)) return 0;
    vector<array<long long, 3>> calendar(p), jobs(n);
    vector<long long> points;
    for (auto& [l, r, c] : calendar) {
        cin >> l >> r >> c; points.push_back(l); points.push_back(r);
    }
    long long total = 0;
    bool impossible = false;
    for (auto& [l, r, work] : jobs) {
        cin >> l >> r >> work;
        points.push_back(l); points.push_back(r); total += work;
        if (work > r - l) impossible = true;
    }
    if (impossible) { cout << -1 << '\n'; return 0; }
    sort(points.begin(), points.end());
    points.erase(unique(points.begin(), points.end()), points.end());
    int blocks = static_cast<int>(points.size()) - 1;
    vector<long long> base(blocks);
    int current = 0;
    for (int j = 0; j < blocks; ++j) {
        while (points[j] >= calendar[current][1]) ++current;
        base[j] = calendar[current][2];
    }
    auto feasible = [&](int extra) {
        int s = n + blocks, t = s + 1;
        Dinic flow(t + 1);
        for (int i = 0; i < n; ++i) {
            auto [l, r, work] = jobs[i];
            flow.add_edge(s, i, work);
            for (int j = 0; j < blocks; ++j)
                if (l <= points[j] && points[j + 1] <= r)
                    flow.add_edge(i, n + j, points[j + 1] - points[j]);
        }
        for (int j = 0; j < blocks; ++j) {
            long long length = points[j + 1] - points[j];
            long long capacity = min(total, (base[j] + extra) * length);
            flow.add_edge(n + j, t, capacity);
        }
        return flow.max_flow(s, t) == total;
    };
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (feasible(mid)) hi = mid;
        else lo = mid + 1;
    }
    cout << lo << '\n';
}
