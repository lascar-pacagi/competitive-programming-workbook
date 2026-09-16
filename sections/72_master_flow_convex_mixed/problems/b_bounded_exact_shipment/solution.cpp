#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF = (1LL << 62);

struct MinCostFlow {
    struct Edge { int to, rev, cap; ll cost; };
    vector<vector<Edge>> graph;

    explicit MinCostFlow(int n) : graph(n) {}

    void add_edge(int u, int v, int cap, ll cost) {
        int a = graph[u].size();
        int b = graph[v].size();
        graph[u].push_back({v, b, cap, cost});
        graph[v].push_back({u, a, 0, -cost});
    }

    pair<int, ll> flow(int source, int sink, int required) {
        int sent = 0;
        ll cost = 0;
        int n = graph.size();
        vector<ll> distance(n);
        vector<int> parent_v(n), parent_e(n);

        while (sent < required) {
            fill(distance.begin(), distance.end(), INF);
            vector<char> queued(n, false);
            queue<int> queue;
            distance[source] = 0;
            queue.push(source);
            queued[source] = true;
            while (!queue.empty()) {
                int u = queue.front();
                queue.pop();
                queued[u] = false;
                for (int i = 0; i < (int)graph[u].size(); ++i) {
                    const Edge& edge = graph[u][i];
                    if (!edge.cap) continue;
                    ll candidate = distance[u] + edge.cost;
                    if (candidate >= distance[edge.to]) continue;
                    distance[edge.to] = candidate;
                    parent_v[edge.to] = u;
                    parent_e[edge.to] = i;
                    if (!queued[edge.to]) {
                        queued[edge.to] = true;
                        queue.push(edge.to);
                    }
                }
            }
            if (distance[sink] == INF) break;
            int add = required - sent;
            for (int v = sink; v != source; v = parent_v[v])
                add = min(add,
                    graph[parent_v[v]][parent_e[v]].cap);
            for (int v = sink; v != source; v = parent_v[v]) {
                Edge& edge = graph[parent_v[v]][parent_e[v]];
                cost += ll(add) * edge.cost;
                edge.cap -= add;
                graph[v][edge.rev].cap += add;
            }
            sent += add;
        }
        return {sent, cost};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, required_flow;
    cin >> n >> m >> required_flow;
    int source_vertex, sink_vertex;
    cin >> source_vertex >> sink_vertex;
    --source_vertex;
    --sink_vertex;

    int super_source = n;
    int super_sink = n + 1;
    MinCostFlow network(n + 2);
    vector<int> balance(n, 0);
    ll mandatory_cost = 0;

    auto add_bounded = [&](int u, int v, int low,
                           int high, ll cost) {
        balance[u] -= low;
        balance[v] += low;
        mandatory_cost += ll(low) * cost;
        network.add_edge(u, v, high - low, cost);
    };

    for (int i = 0; i < m; ++i) {
        int u, v, low, high;
        ll cost;
        cin >> u >> v >> low >> high >> cost;
        add_bounded(u - 1, v - 1, low, high, cost);
    }
    add_bounded(sink_vertex, source_vertex,
                required_flow, required_flow, 0);

    int required = 0;
    for (int vertex = 0; vertex < n; ++vertex) {
        if (balance[vertex] > 0) {
            network.add_edge(super_source, vertex,
                             balance[vertex], 0);
            required += balance[vertex];
        } else if (balance[vertex] < 0) {
            network.add_edge(vertex, super_sink,
                             -balance[vertex], 0);
        }
    }

    auto [sent, extra_cost] =
        network.flow(super_source, super_sink, required);
    if (sent != required)
        cout << "IMPOSSIBLE\n";
    else
        cout << mandatory_cost + extra_cost << '\n';
}
