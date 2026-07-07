#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, budget;
    if (!(cin >> n >> budget)) return 0;
    vector<int> need(n);
    vector<long long> value(n);
    for (int i = 0; i < n; i++) cin >> need[i] >> value[i];
    vector<vector<int>> children(n);
    for (int child = 1; child < n; child++) {
        int parent;
        cin >> parent;
        children[parent - 1].push_back(child);
    }

    vector<int> order = {0};
    for (int i = 0; i < (int)order.size(); i++) {
        int u = order[i];
        for (int v : children[u]) order.push_back(v);
    }

    const long long NEG = -(1LL << 60);
    vector<vector<long long>> dp(n, vector<long long>(budget + 1, NEG));
    for (int idx = n - 1; idx >= 0; idx--) {
        int u = order[idx];
        if (need[u] <= budget) dp[u][need[u]] = value[u];
        for (int v : children[u]) {
            vector<long long> merged = dp[u];
            for (int used = 0; used <= budget; used++) {
                if (dp[u][used] == NEG) continue;
                for (int add = 1; used + add <= budget; add++) {
                    if (dp[v][add] == NEG) continue;
                    merged[used + add] = max(merged[used + add], dp[u][used] + dp[v][add]);
                }
            }
            dp[u].swap(merged);
        }
    }

    long long answer = 0;
    for (long long x : dp[0]) answer = max(answer, x);
    cout << answer << '\n';
    return 0;
}
