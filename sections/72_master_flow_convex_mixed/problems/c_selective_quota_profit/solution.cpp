#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF = (1LL << 62);

struct MCF {
    struct Edge { int to, rev, cap; ll cost; };
    vector<vector<Edge>> graph;
    explicit MCF(int n) : graph(n) {}

    pair<int, int> add_edge(int u, int v, int cap, ll cost) {
        int index = graph[u].size();
        graph[u].push_back({v, (int)graph[v].size(), cap, cost});
        graph[v].push_back({u, index, 0, -cost});
        return {u, index};
    }

    pair<int, ll> flow(int source, int sink, int limit) {
        int n = graph.size();
        vector<ll> potential(n, INF), distance(n);
        potential[source] = 0;
        for (int repeat = 0; repeat < n; ++repeat) {
            bool changed = false;
            for (int u = 0; u < n; ++u) {
                if (potential[u] == INF) continue;
                for (const Edge& edge : graph[u]) {
                    if (edge.cap
                        && potential[edge.to] > potential[u] + edge.cost) {
                        potential[edge.to] = potential[u] + edge.cost;
                        changed = true;
                    }
                }
            }
            if (!changed) break;
        }
        for (ll& value : potential)
            if (value == INF) value = 0;

        int sent = 0;
        ll total_cost = 0;
        vector<int> parent_v(n), parent_e(n);
        while (sent < limit) {
            fill(distance.begin(), distance.end(), INF);
            distance[source] = 0;
            priority_queue<pair<ll, int>,
                vector<pair<ll, int>>, greater<pair<ll, int>>> queue;
            queue.push({0, source});
            while (!queue.empty()) {
                auto [current, u] = queue.top();
                queue.pop();
                if (current != distance[u]) continue;
                for (int i = 0; i < (int)graph[u].size(); ++i) {
                    const Edge& edge = graph[u][i];
                    if (!edge.cap) continue;
                    ll next = current + edge.cost
                            + potential[u] - potential[edge.to];
                    if (next >= distance[edge.to]) continue;
                    distance[edge.to] = next;
                    parent_v[edge.to] = u;
                    parent_e[edge.to] = i;
                    queue.push({next, edge.to});
                }
            }
            if (distance[sink] == INF) break;
            for (int v = 0; v < n; ++v)
                if (distance[v] < INF) potential[v] += distance[v];
            int add = limit - sent;
            for (int v = sink; v != source; v = parent_v[v])
                add = min(add,
                    graph[parent_v[v]][parent_e[v]].cap);
            for (int v = sink; v != source; v = parent_v[v]) {
                Edge& edge = graph[parent_v[v]][parent_e[v]];
                total_cost += ll(add) * edge.cost;
                edge.cap -= add;
                graph[v][edge.rev].cap += add;
            }
            sent += add;
        }
        return {sent, total_cost};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, projects, m, chosen;
    cin >> n >> projects >> m >> chosen;
    vector<int> low(projects), high(projects);
    int mandatory_count = 0;
    for (int j = 0; j < projects; ++j) {
        cin >> low[j] >> high[j];
        mandatory_count += low[j];
    }
    struct Choice { int worker, project, profit; };
    vector<Choice> choices(m);
    int maximum_profit = 0;
    for (Choice& choice : choices) {
        cin >> choice.worker >> choice.project >> choice.profit;
        --choice.worker;
        --choice.project;
        maximum_profit = max(maximum_profit, choice.profit);
    }

    int source = n + projects;
    int sink = source + 1;
    MCF network(sink + 1);
    for (int worker = 0; worker < n; ++worker)
        network.add_edge(source, worker, 1, 0);
    for (const Choice& choice : choices)
        network.add_edge(choice.worker, n + choice.project,
                         1, -choice.profit);

    ll big = ll(chosen + 1) * (maximum_profit + 1LL);
    vector<pair<int, int>> mandatory;
    for (int project = 0; project < projects; ++project) {
        mandatory.push_back(network.add_edge(
            n + project, sink, low[project], -big));
        network.add_edge(n + project, sink,
                         high[project] - low[project], 0);
    }

    auto [sent, cost] = network.flow(source, sink, chosen);
    bool possible = sent == chosen;
    for (auto [u, index] : mandatory)
        possible &= network.graph[u][index].cap == 0;
    if (!possible)
        cout << "IMPOSSIBLE\n";
    else
        cout << -cost - big * mandatory_count << '\n';
}
