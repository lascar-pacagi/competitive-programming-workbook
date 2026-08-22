#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int u, v, color;
    long long weight;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, need;
    cin >> n >> m >> need;
    vector<Edge> edges(m);
    vector<int> colors;
    vector<long long> weights;
    for (auto &[u, v, color, weight] : edges) {
        cin >> u >> v >> color >> weight;
        --u;
        --v;
        colors.push_back(color);
        weights.push_back(weight);
    }
    sort(colors.begin(), colors.end());
    colors.erase(unique(colors.begin(), colors.end()), colors.end());
    for (auto &edge : edges) {
        edge.color = lower_bound(colors.begin(), colors.end(), edge.color)
                   - colors.begin();
    }
    sort(weights.begin(), weights.end());
    weights.erase(unique(weights.begin(), weights.end()), weights.end());

    auto feasible = [&](long long limit) {
        vector<char> allowed(m), chosen(m);
        for (int i = 0; i < m; ++i) allowed[i] = edges[i].weight <= limit;

        for (int size = 0; size < need; ++size) {
            vector<vector<pair<int, int>>> forest(n);
            vector<int> color_edge(colors.size(), -1);
            for (int i = 0; i < m; ++i) if (chosen[i]) {
                forest[edges[i].u].push_back({edges[i].v, i});
                forest[edges[i].v].push_back({edges[i].u, i});
                color_edge[edges[i].color] = i;
            }

            vector<vector<int>> next(m);
            vector<char> source(m), target(m);
            for (int y = 0; y < m; ++y) if (allowed[y] && !chosen[y]) {
                vector<int> parent_vertex(n, -1), parent_edge(n, -1);
                queue<int> vertices;
                parent_vertex[edges[y].u] = edges[y].u;
                vertices.push(edges[y].u);
                while (!vertices.empty() && parent_vertex[edges[y].v] == -1) {
                    int u = vertices.front();
                    vertices.pop();
                    for (auto [v, index] : forest[u]) {
                        if (parent_vertex[v] != -1) continue;
                        parent_vertex[v] = u;
                        parent_edge[v] = index;
                        vertices.push(v);
                    }
                }
                if (parent_vertex[edges[y].v] == -1) {
                    source[y] = true;
                } else {
                    for (int v = edges[y].v; v != edges[y].u;
                         v = parent_vertex[v]) {
                        next[parent_edge[v]].push_back(y);
                    }
                }

                int same = color_edge[edges[y].color];
                if (same == -1) target[y] = true;
                else next[y].push_back(same);
            }

            queue<int> queue_nodes;
            vector<int> parent(m, -2);
            for (int i = 0; i < m; ++i) if (source[i]) {
                parent[i] = -1;
                queue_nodes.push(i);
            }
            int finish = -1;
            while (!queue_nodes.empty() && finish == -1) {
                int u = queue_nodes.front();
                queue_nodes.pop();
                if (target[u]) {
                    finish = u;
                    break;
                }
                for (int v : next[u]) if (parent[v] == -2) {
                    parent[v] = u;
                    queue_nodes.push(v);
                }
            }
            if (finish == -1) return false;
            for (int at = finish; at != -1; at = parent[at]) chosen[at] ^= 1;
        }
        return true;
    };

    if (weights.empty() || !feasible(weights.back())) {
        cout << -1 << '\n';
        return 0;
    }
    int low = 0, high = (int)weights.size() - 1;
    while (low < high) {
        int middle = (low + high) / 2;
        if (feasible(weights[middle])) high = middle;
        else low = middle + 1;
    }
    cout << weights[low] << '\n';
}
