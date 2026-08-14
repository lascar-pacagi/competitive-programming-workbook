#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> cost(n);
    for (long long& value : cost)
        cin >> value;

    vector<vector<int>> graph(n);
    for (int edge = 1; edge < n; ++edge) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<int> parent(n, -2), order = {0};
    parent[0] = -1;
    for (int index = 0; index < n; ++index) {
        int u = order[index];
        for (int v : graph[u]) {
            if (v == parent[u])
                continue;
            parent[v] = u;
            order.push_back(v);
        }
    }

    const long long INF = 4'000'000'000'000'000'000LL;
    // State 0: u has a guard.
    // State 1: u has no guard and is protected by a child.
    // State 2: u is not protected yet and needs its parent to have a guard.
    vector<array<long long, 3>> dp(n);

    for (int index = n - 1; index >= 0; --index) {
        int u = order[index];
        long long selected = cost[u];
        long long covered_base = 0;
        long long force_guard_child = INF;
        long long awaiting_parent = 0;

        for (int v : graph[u]) {
            if (parent[v] != u)
                continue;

            selected += min({dp[v][0], dp[v][1], dp[v][2]});

            long long best_covered_child = min(dp[v][0], dp[v][1]);
            covered_base += best_covered_child;
            force_guard_child = min(force_guard_child,
                                    dp[v][0] - best_covered_child);

            if (awaiting_parent == INF || dp[v][1] >= INF / 2)
                awaiting_parent = INF;
            else
                awaiting_parent += dp[v][1];
        }

        dp[u][0] = selected;
        dp[u][1] = (force_guard_child == INF
                    ? INF : covered_base + force_guard_child);
        dp[u][2] = awaiting_parent;
    }

    // The root has no parent, so it cannot remain in state 2.
    cout << min(dp[0][0], dp[0][1]) << '\n';
}
