#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

constexpr int64 INF = 4'000'000'000'000'000'000LL;

struct Dinic {
    struct Edge { int to, reverse; int64 capacity; };
    int n;
    vector<vector<Edge>> graph;
    vector<int> level, next_edge;

    explicit Dinic(int n) : n(n), graph(n), level(n), next_edge(n) {}

    void add_edge(int u, int v, int64 capacity) {
        graph[u].push_back({v, static_cast<int>(graph[v].size()), capacity});
        graph[v].push_back({u, static_cast<int>(graph[u].size()) - 1, 0});
    }

    bool bfs(int source, int sink) {
        fill(level.begin(), level.end(), -1);
        queue<int> queue;
        level[source] = 0;
        queue.push(source);
        while (!queue.empty()) {
            int u = queue.front();
            queue.pop();
            for (const Edge &edge : graph[u])
                if (edge.capacity > 0 && level[edge.to] == -1) {
                    level[edge.to] = level[u] + 1;
                    queue.push(edge.to);
                }
        }
        return level[sink] != -1;
    }

    int64 dfs(int u, int sink, int64 pushed) {
        if (u == sink) return pushed;
        for (int &index = next_edge[u]; index < static_cast<int>(graph[u].size()); ++index) {
            Edge &edge = graph[u][index];
            if (edge.capacity == 0 || level[edge.to] != level[u] + 1) continue;
            int64 sent = dfs(edge.to, sink, min(pushed, edge.capacity));
            if (sent == 0) continue;
            edge.capacity -= sent;
            graph[edge.to][edge.reverse].capacity += sent;
            return sent;
        }
        return 0;
    }

    int64 max_flow(int source, int sink) {
        int64 result = 0;
        while (bfs(source, sink)) {
            fill(next_edge.begin(), next_edge.end(), 0);
            while (int64 pushed = dfs(source, sink, INF)) result += pushed;
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, target;
    cin >> n >> m >> target;
    vector<int64> profit(n);
    for (int64 &x : profit) cin >> x;
    vector<pair<int, int>> dependencies(m);
    for (auto &[u, v] : dependencies) {
        cin >> u >> v;
        --u;
        --v;
    }

    auto solve = [&](int64 penalty) {
        int source = n, sink = n + 1;
        Dinic flow(n + 2);
        for (int vertex = 0; vertex < n; ++vertex) {
            int64 adjusted = profit[vertex] - penalty;
            if (adjusted > 0) flow.add_edge(source, vertex, adjusted);
            else if (adjusted < 0) flow.add_edge(vertex, sink, -adjusted);
        }
        for (auto [u, v] : dependencies) flow.add_edge(u, v, INF);
        flow.max_flow(source, sink);
        vector<bool> reachable(n + 2);
        queue<int> queue;
        reachable[source] = true;
        queue.push(source);
        while (!queue.empty()) {
            int u = queue.front();
            queue.pop();
            for (const auto &edge : flow.graph[u])
                if (edge.capacity > 0 && !reachable[edge.to]) {
                    reachable[edge.to] = true;
                    queue.push(edge.to);
                }
        }
        int size = 0;
        int64 original_profit = 0;
        for (int vertex = 0; vertex < n; ++vertex)
            if (reachable[vertex]) {
                ++size;
                original_profit += profit[vertex];
            }
        return pair{size, original_profit};
    };

    int64 low = -1'000'000'001LL, high = 1'000'000'001LL;
    while (low < high) {
        int64 middle = low + (high - low) / 2;
        if (solve(middle).first <= target) high = middle;
        else low = middle + 1;
    }
    auto [size, answer] = solve(low);
    if (size != target) {
        // The input promise guarantees this branch is unreachable.
        return 1;
    }
    cout << answer << '\n';
}
