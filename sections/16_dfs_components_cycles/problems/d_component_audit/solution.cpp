#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> graph(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<char> seen(n, false);
    int tree_components = 0;
    int cyclic_components = 0;

    for (int start = 0; start < n; ++start) {
        if (seen[start]) continue;

        long long vertices = 0;
        long long degree_sum = 0;
        vector<int> stack = {start};
        seen[start] = true;

        while (!stack.empty()) {
            int u = stack.back();
            stack.pop_back();
            ++vertices;
            degree_sum += graph[u].size();
            for (int v : graph[u]) {
                if (!seen[v]) {
                    seen[v] = true;
                    stack.push_back(v);
                }
            }
        }

        long long edges = degree_sum / 2;
        if (edges == vertices - 1) {
            ++tree_components;
        } else {
            ++cyclic_components;
        }
    }

    cout << tree_components << ' ' << cyclic_components << '\n';
    return 0;
}
