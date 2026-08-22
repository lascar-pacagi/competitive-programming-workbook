#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
const int64 INF = (1LL << 62);

struct MinCostFlow {
    struct Edge {
        int to, reverse, capacity;
        int64 cost;
    };
    vector<vector<Edge>> graph;

    explicit MinCostFlow(int n) : graph(n) {}

    void add_edge(int u, int v, int capacity, int64 cost) {
        int ui = graph[u].size();
        int vi = graph[v].size();
        graph[u].push_back({v, vi, capacity, cost});
        graph[v].push_back({u, ui, 0, -cost});
    }

    pair<int, int64> flow(int source, int sink, int required) {
        int n = graph.size();
        int sent = 0;
        int64 total_cost = 0;
        vector<int64> potential(n), distance(n);
        vector<int> previous_vertex(n), previous_edge(n);

        while (sent < required) {
            fill(distance.begin(), distance.end(), INF);
            distance[source] = 0;
            priority_queue<pair<int64, int>, vector<pair<int64, int>>,
                           greater<pair<int64, int>>> queue;
            queue.push({0, source});

            while (!queue.empty()) {
                auto [current_distance, u] = queue.top();
                queue.pop();
                if (current_distance != distance[u]) continue;
                for (int index = 0; index < (int)graph[u].size(); ++index) {
                    const Edge& edge = graph[u][index];
                    if (!edge.capacity) continue;
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
            for (int v = 0; v < n; ++v) {
                if (distance[v] < INF) potential[v] += distance[v];
            }

            int add = required - sent;
            for (int v = sink; v != source; v = previous_vertex[v]) {
                add = min(add, graph[previous_vertex[v]][previous_edge[v]].capacity);
            }
            for (int v = sink; v != source; v = previous_vertex[v]) {
                Edge& edge = graph[previous_vertex[v]][previous_edge[v]];
                total_cost += int64(add) * edge.cost;
                edge.capacity -= add;
                graph[v][edge.reverse].capacity += add;
            }
            sent += add;
        }
        return {sent, total_cost};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    int source = n;
    int sink = n + 1;
    MinCostFlow network(n + 2);
    vector<int> balance(n);
    int64 mandatory_cost = 0;

    for (int edge = 0; edge < m; ++edge) {
        int u, v, low, high, cost;
        cin >> u >> v >> low >> high >> cost;
        --u;
        --v;
        balance[u] -= low;
        balance[v] += low;
        mandatory_cost += int64(low) * cost;
        network.add_edge(u, v, high - low, cost);
    }

    int required = 0;
    for (int v = 0; v < n; ++v) {
        if (balance[v] > 0) {
            network.add_edge(source, v, balance[v], 0);
            required += balance[v];
        } else if (balance[v] < 0) {
            network.add_edge(v, sink, -balance[v], 0);
        }
    }

    auto [sent, extra_cost] = network.flow(source, sink, required);
    if (sent != required) cout << "IMPOSSIBLE\n";
    else cout << mandatory_cost + extra_cost << '\n';
}
