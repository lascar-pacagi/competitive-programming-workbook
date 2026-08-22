#include <bits/stdc++.h>
using namespace std;

class Blossom {
    int n;
    vector<vector<int>> graph;
    vector<int> match, parent, base, queue_nodes;
    vector<char> used, in_blossom;

    int lca(int a, int b) {
        vector<char> seen(n, false);
        while (true) {
            a = base[a];
            seen[a] = true;
            if (match[a] == -1) break;
            a = parent[match[a]];
        }
        while (true) {
            b = base[b];
            if (seen[b]) return b;
            b = parent[match[b]];
        }
    }

    void mark_path(int v, int blossom_base, int child) {
        while (base[v] != blossom_base) {
            in_blossom[base[v]] = in_blossom[base[match[v]]] = true;
            parent[v] = child;
            child = match[v];
            v = parent[match[v]];
        }
    }

    bool augment_from(int root) {
        used.assign(n, false);
        parent.assign(n, -1);
        iota(base.begin(), base.end(), 0);
        queue_nodes.clear();
        queue_nodes.push_back(root);
        used[root] = true;
        for (int head = 0; head < (int)queue_nodes.size(); ++head) {
            int v = queue_nodes[head];
            for (int u : graph[v]) {
                if (base[v] == base[u] || match[v] == u) continue;
                if (u == root || (match[u] != -1 && parent[match[u]] != -1)) {
                    int blossom_base = lca(v, u);
                    in_blossom.assign(n, false);
                    mark_path(v, blossom_base, u);
                    mark_path(u, blossom_base, v);
                    for (int x = 0; x < n; ++x) if (in_blossom[base[x]]) {
                        base[x] = blossom_base;
                        if (!used[x]) {
                            used[x] = true;
                            queue_nodes.push_back(x);
                        }
                    }
                } else if (parent[u] == -1) {
                    parent[u] = v;
                    if (match[u] == -1) {
                        int x = u;
                        while (x != -1) {
                            int previous = parent[x];
                            int next = previous == -1 ? -1 : match[previous];
                            match[x] = previous;
                            if (previous != -1) match[previous] = x;
                            x = next;
                        }
                        return true;
                    }
                    u = match[u];
                    used[u] = true;
                    queue_nodes.push_back(u);
                }
            }
        }
        return false;
    }

public:
    explicit Blossom(vector<vector<int>> adjacency)
        : n(adjacency.size()), graph(move(adjacency)), match(n, -1),
          parent(n), base(n), used(n), in_blossom(n) {}

    int maximum_matching() {
        int size = 0;
        for (int v = 0; v < n; ++v) {
            if (match[v] == -1 && augment_from(v)) ++size;
        }
        return size;
    }
};

struct Edge {
    int u, v;
    long long difficulty;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    cin >> n >> m >> q;
    vector<Edge> edges(m);
    vector<long long> thresholds;
    for (auto &[u, v, difficulty] : edges) {
        cin >> u >> v >> difficulty;
        --u;
        --v;
        thresholds.push_back(difficulty);
    }
    vector<int> queries(q);
    vector<char> needed(n / 2 + 1, false);
    for (int &k : queries) {
        cin >> k;
        needed[k] = true;
    }
    sort(thresholds.begin(), thresholds.end());
    thresholds.erase(unique(thresholds.begin(), thresholds.end()), thresholds.end());
    if (thresholds.empty()) {
        while (q--) cout << -1 << '\n';
        return 0;
    }

    vector<int> low(n / 2 + 1, 0), high(n / 2 + 1, thresholds.size());
    unordered_map<int, int> rank_cache;
    auto rank_at = [&](int index) {
        auto found = rank_cache.find(index);
        if (found != rank_cache.end()) return found->second;
        vector<vector<int>> graph(n);
        for (const auto &edge : edges) if (edge.difficulty <= thresholds[index]) {
            graph[edge.u].push_back(edge.v);
            graph[edge.v].push_back(edge.u);
        }
        int rank = Blossom(move(graph)).maximum_matching();
        rank_cache[index] = rank;
        return rank;
    };

    while (true) {
        map<int, vector<int>> groups;
        for (int k = 1; k <= n / 2; ++k) {
            if (needed[k] && low[k] < high[k]) {
                int middle = (low[k] + high[k]) / 2;
                groups[middle].push_back(k);
            }
        }
        if (groups.empty()) break;
        for (const auto &[middle, sizes] : groups) {
            int rank = rank_at(middle);
            for (int k : sizes) {
                if (rank >= k) high[k] = middle;
                else low[k] = middle + 1;
            }
        }
    }
    for (int k : queries) {
        if (low[k] == (int)thresholds.size()) cout << -1 << '\n';
        else cout << thresholds[low[k]] << '\n';
    }
}
