#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

struct Edge {
    int to, reverse;
    int64 capacity, cost;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    int source = n, sink = n + 1;
    vector<vector<Edge>> graph(n + 2);
    auto add_edge = [&](int u, int v, int64 capacity, int64 cost) {
        Edge forward{v, static_cast<int>(graph[v].size()), capacity, cost};
        Edge backward{u, static_cast<int>(graph[u].size()), 0, -cost};
        graph[u].push_back(forward);
        graph[v].push_back(backward);
    };

    vector<int64> balance(n);
    int64 base_cost = 0;
    for (int edge = 0; edge < m; ++edge) {
        int u, v;
        int64 lower, upper, c, d;
        cin >> u >> v >> lower >> upper >> c >> d;
        --u;
        --v;
        balance[u] -= lower;
        balance[v] += lower;
        base_cost += c * lower + d * lower * (lower - 1) / 2;
        for (int64 amount = lower; amount < upper; ++amount)
            add_edge(u, v, 1, c + d * amount);
    }
    int64 required = 0;
    for (int vertex = 0; vertex < n; ++vertex) {
        if (balance[vertex] > 0) {
            add_edge(source, vertex, balance[vertex], 0);
            required += balance[vertex];
        } else if (balance[vertex] < 0) {
            add_edge(vertex, sink, -balance[vertex], 0);
        }
    }

    const int64 INF = 4'000'000'000'000'000'000LL;
    vector<int64> potential(n + 2), distance(n + 2);
    vector<int> previous_vertex(n + 2), previous_edge(n + 2);
    int64 sent = 0, extra_cost = 0;
    while (sent < required) {
        fill(distance.begin(), distance.end(), INF);
        distance[source] = 0;
        priority_queue<pair<int64, int>, vector<pair<int64, int>>, greater<>> queue;
        queue.push({0, source});
        while (!queue.empty()) {
            auto [current_distance, u] = queue.top();
            queue.pop();
            if (current_distance != distance[u]) continue;
            for (int index = 0; index < static_cast<int>(graph[u].size()); ++index) {
                const Edge &edge = graph[u][index];
                if (edge.capacity == 0) continue;
                int64 candidate = current_distance + edge.cost
                                + potential[u] - potential[edge.to];
                if (candidate < distance[edge.to]) {
                    distance[edge.to] = candidate;
                    previous_vertex[edge.to] = u;
                    previous_edge[edge.to] = index;
                    queue.push({candidate, edge.to});
                }
            }
        }
        if (distance[sink] == INF) break;
        for (int vertex = 0; vertex < n + 2; ++vertex)
            if (distance[vertex] != INF) potential[vertex] += distance[vertex];
        int64 pushed = required - sent;
        for (int v = sink; v != source; v = previous_vertex[v])
            pushed = min(pushed, graph[previous_vertex[v]][previous_edge[v]].capacity);
        for (int v = sink; v != source; v = previous_vertex[v]) {
            int u = previous_vertex[v], index = previous_edge[v];
            Edge &edge = graph[u][index];
            extra_cost += pushed * edge.cost;
            edge.capacity -= pushed;
            graph[v][edge.reverse].capacity += pushed;
        }
        sent += pushed;
    }
    if (sent != required) cout << "IMPOSSIBLE\n";
    else cout << base_cost + extra_cost << '\n';
}
