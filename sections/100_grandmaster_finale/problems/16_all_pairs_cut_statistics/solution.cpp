#include <bits/stdc++.h>
using namespace std;

struct InputEdge {
    int u, v;
    long long capacity;
};

class Dinic {
    struct Edge {
        int to, reverse;
        long long capacity;
    };
    int n;
    vector<vector<Edge>> graph;
    vector<int> level, next_edge;

    long long send(int u, int sink, long long pushed) {
        if (u == sink) return pushed;
        for (int &i = next_edge[u]; i < (int)graph[u].size(); ++i) {
            Edge &edge = graph[u][i];
            if (edge.capacity == 0 || level[edge.to] != level[u] + 1) continue;
            long long flow = send(edge.to, sink, min(pushed, edge.capacity));
            if (flow == 0) continue;
            edge.capacity -= flow;
            graph[edge.to][edge.reverse].capacity += flow;
            return flow;
        }
        return 0;
    }

public:
    explicit Dinic(int vertices) : n(vertices), graph(n), level(n), next_edge(n) {}

    void add_undirected(int u, int v, long long capacity) {
        int ru = graph[v].size(), rv = graph[u].size();
        graph[u].push_back({v, ru, capacity});
        graph[v].push_back({u, rv, capacity});
    }

    long long max_flow(int source, int sink) {
        long long answer = 0;
        while (true) {
            fill(level.begin(), level.end(), -1);
            queue<int> queue_nodes;
            level[source] = 0;
            queue_nodes.push(source);
            while (!queue_nodes.empty()) {
                int u = queue_nodes.front();
                queue_nodes.pop();
                for (const Edge &edge : graph[u]) {
                    if (edge.capacity > 0 && level[edge.to] == -1) {
                        level[edge.to] = level[u] + 1;
                        queue_nodes.push(edge.to);
                    }
                }
            }
            if (level[sink] == -1) break;
            fill(next_edge.begin(), next_edge.end(), 0);
            while (long long flow = send(source, sink, (1LL << 62))) {
                answer += flow;
            }
        }
        return answer;
    }

    vector<char> source_side(int source) const {
        vector<char> seen(n, false);
        queue<int> queue_nodes;
        seen[source] = true;
        queue_nodes.push(source);
        while (!queue_nodes.empty()) {
            int u = queue_nodes.front();
            queue_nodes.pop();
            for (const Edge &edge : graph[u]) {
                if (edge.capacity > 0 && !seen[edge.to]) {
                    seen[edge.to] = true;
                    queue_nodes.push(edge.to);
                }
            }
        }
        return seen;
    }
};

class DSU {
    vector<int> parent, size;
public:
    explicit DSU(int n) : parent(n), size(n, 1) { iota(parent.begin(), parent.end(), 0); }
    int find(int x) { return parent[x] == x ? x : parent[x] = find(parent[x]); }
    long long unite_pairs(int a, int b) {
        a = find(a); b = find(b);
        if (a == b) return 0;
        if (size[a] < size[b]) swap(a, b);
        long long added = 1LL * size[a] * size[b];
        parent[b] = a;
        size[a] += size[b];
        return added;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    cin >> n >> m >> q;
    vector<InputEdge> input_edges(m);
    for (auto &[u, v, capacity] : input_edges) {
        cin >> u >> v >> capacity;
        --u; --v;
    }

    vector<int> parent(n, 0);
    vector<long long> cut_value(n, 0);
    for (int s = 1; s < n; ++s) {
        int t = parent[s];
        Dinic flow(n);
        for (const auto &edge : input_edges) {
            flow.add_undirected(edge.u, edge.v, edge.capacity);
        }
        long long value = flow.max_flow(s, t);
        vector<char> side = flow.source_side(s);
        for (int v = s + 1; v < n; ++v) {
            if (parent[v] == t && side[v]) parent[v] = s;
        }
        if (side[parent[t]]) {
            parent[s] = parent[t];
            parent[t] = s;
            cut_value[s] = cut_value[t];
            cut_value[t] = value;
        } else {
            cut_value[s] = value;
        }
    }

    vector<tuple<long long, int, int>> tree_edges;
    for (int v = 1; v < n; ++v) {
        tree_edges.push_back({cut_value[v], v, parent[v]});
    }
    sort(tree_edges.begin(), tree_edges.end(), greater<>());
    vector<pair<long long, int>> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].first;
        queries[i].second = i;
    }
    sort(queries.begin(), queries.end(), greater<>());
    vector<long long> answers(q);
    DSU dsu(n);
    long long pairs = 0;
    int edge_index = 0;
    for (auto [threshold, query_index] : queries) {
        while (edge_index < (int)tree_edges.size()
               && get<0>(tree_edges[edge_index]) >= threshold) {
            auto [weight, u, v] = tree_edges[edge_index++];
            pairs += dsu.unite_pairs(u, v);
        }
        answers[query_index] = pairs;
    }
    for (long long answer : answers) cout << answer << '\n';
}
