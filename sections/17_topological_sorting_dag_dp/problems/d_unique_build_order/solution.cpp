#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> graph(n + 1);
    vector<int> indegree(n + 1, 0);
    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        ++indegree[b];
    }

    queue<int> available;
    for (int step = 1; step <= n; ++step) {
        if (indegree[step] == 0) {
            available.push(step);
        }
    }

    bool ambiguous = false;
    vector<int> order;
    while (!available.empty()) {
        if (available.size() > 1) {
            ambiguous = true;
        }

        int u = available.front();
        available.pop();
        order.push_back(u);

        for (int v : graph[u]) {
            --indegree[v];
            if (indegree[v] == 0) {
                available.push(v);
            }
        }
    }

    if (static_cast<int>(order.size()) != n) {
        cout << "IMPOSSIBLE\n";
    } else if (ambiguous) {
        cout << "AMBIGUOUS\n";
    } else {
        cout << "UNIQUE\n";
        for (int i = 0; i < n; ++i) {
            cout << order[i] << (i + 1 == n ? '\n' : ' ');
        }
    }
}
