#include <bits/stdc++.h>
using namespace std;

struct Dinic {
    struct Edge {
        int to, reverse;
        long long capacity;
    };

    vector<vector<Edge>> graph;
    vector<int> level, next_edge;

    explicit Dinic(int n) : graph(n), level(n), next_edge(n) {}

    void add_edge(int from, int to, long long capacity) {
        Edge forward{to, (int)graph[to].size(), capacity};
        Edge backward{from, (int)graph[from].size(), 0};
        graph[from].push_back(forward);
        graph[to].push_back(backward);
    }

    bool build_levels(int source, int sink) {
        fill(level.begin(), level.end(), -1);
        queue<int> queue;
        level[source] = 0;
        queue.push(source);
        while (!queue.empty()) {
            int vertex = queue.front();
            queue.pop();
            for (const Edge& edge : graph[vertex]) {
                if (edge.capacity > 0 && level[edge.to] == -1) {
                    level[edge.to] = level[vertex] + 1;
                    queue.push(edge.to);
                }
            }
        }
        return level[sink] != -1;
    }

    long long send_flow(int vertex, int sink, long long pushed) {
        if (vertex == sink) return pushed;
        for (int& edge_index = next_edge[vertex];
             edge_index < (int)graph[vertex].size(); edge_index++) {
            Edge& edge = graph[vertex][edge_index];
            if (edge.capacity == 0 || level[edge.to] != level[vertex] + 1) continue;
            long long flow = send_flow(edge.to, sink, min(pushed, edge.capacity));
            if (flow == 0) continue;
            edge.capacity -= flow;
            graph[edge.to][edge.reverse].capacity += flow;
            return flow;
        }
        return 0;
    }

    long long max_flow(int source, int sink) {
        long long total = 0;
        const long long INF = numeric_limits<long long>::max() / 4;
        while (build_levels(source, sink)) {
            fill(next_edge.begin(), next_edge.end(), 0);
            while (long long pushed = send_flow(source, sink, INF)) total += pushed;
        }
        return total;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> profit(n);
    long long positive_total = 0;
    for (long long& value : profit) {
        cin >> value;
        if (value > 0) positive_total += value;
    }

    int source = n;
    int sink = n + 1;
    Dinic flow(n + 2);
    long long inf = positive_total + 1;
    for (int project = 0; project < n; project++) {
        if (profit[project] > 0) flow.add_edge(source, project, profit[project]);
        if (profit[project] < 0) flow.add_edge(project, sink, -profit[project]);
    }
    for (int i = 0; i < m; i++) {
        int project, prerequisite;
        cin >> project >> prerequisite;
        flow.add_edge(project - 1, prerequisite - 1, inf);
    }

    cout << positive_total - flow.max_flow(source, sink) << '\n';
    return 0;
}
