#pragma once
#include <cassert>
#include <queue>
#include <utility>
#include <vector>

struct BipartiteMatching {
    std::vector<std::vector<int>> adj;
    std::vector<int> left, right;

    BipartiteMatching(int left_count, int right_count)
        : adj(left_count), left(left_count, -1), right(right_count, -1) {}

    void add_edge(int u, int v) {
        assert(0 <= u && u < static_cast<int>(left.size()));
        assert(0 <= v && v < static_cast<int>(right.size()));
        adj[u].push_back(v);
    }

    bool augment(int root) {
        std::vector<int> previous(right.size(), -1);
        std::vector<bool> seen(left.size(), false);
        std::queue<int> queue;
        seen[root] = true;
        queue.push(root);
        while (!queue.empty()) {
            int u = queue.front();
            queue.pop();
            for (int v : adj[u]) {
                if (previous[v] != -1) continue;
                previous[v] = u;
                int owner = right[v];
                if (owner == -1) {
                    while (v != -1) {
                        u = previous[v];
                        int old = left[u];
                        left[u] = v;
                        right[v] = u;
                        v = old;
                    }
                    return true;
                }
                if (!seen[owner]) {
                    seen[owner] = true;
                    queue.push(owner);
                }
            }
        }
        return false;
    }

    std::vector<std::pair<int, int>> maximum_matching() {
        for (int root = 0; root < static_cast<int>(left.size()); ++root)
            if (left[root] == -1) augment(root);
        std::vector<std::pair<int, int>> pairs;
        for (int u = 0; u < static_cast<int>(left.size()); ++u)
            if (left[u] != -1) pairs.push_back({u, left[u]});
        return pairs;
    }
};
