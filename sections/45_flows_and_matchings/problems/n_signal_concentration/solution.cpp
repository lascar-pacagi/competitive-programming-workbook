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
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> cost(n);
    long long weight = 0;
    for (auto& x : cost) { cin >> x; weight += x; }
    vector<tuple<int, int, long long>> links(m);
    long long reward = 0;
    for (auto& [u, v, w] : links) { cin >> u >> v >> w; --u; --v; reward += w; }
    if (reward == 0) { cout << "0 1\n"; return 0; }
    long long scale = weight * weight + 1;
    long long scaled_reward = scale * reward;
    auto evaluate = [&](long long price, vector<bool>* chosen) {
        int s = n + m, t = s + 1;
        Dinic flow(t + 1);
        for (int v = 0; v < n; ++v) flow.add_edge(v, t, price * cost[v]);
        for (int j = 0; j < m; ++j) {
            auto [u, v, w] = links[j];
            int a = n + j;
            flow.add_edge(s, a, scale * w);
            flow.add_edge(a, u, scaled_reward + 1);
            flow.add_edge(a, v, scaled_reward + 1);
        }
        bool positive = scaled_reward - flow.max_flow(s, t) > 0;
        if (chosen) *chosen = flow.reachable(s);
        return positive;
    };
    long long lo = 0, hi = scaled_reward + 1;
    while (hi - lo > 1) {
        long long mid = lo + (hi - lo) / 2;
        if (evaluate(mid, nullptr)) lo = mid;
        else hi = mid;
    }
    vector<bool> chosen;
    evaluate(lo, &chosen);
    long long numerator = 0, denominator = 0;
    for (int v = 0; v < n; ++v) if (chosen[v]) denominator += cost[v];
    for (auto [u, v, w] : links)
        if (chosen[u] && chosen[v]) numerator += w;
    long long g = gcd(numerator, denominator);
    cout << numerator / g << ' ' << denominator / g << '\n';
}
