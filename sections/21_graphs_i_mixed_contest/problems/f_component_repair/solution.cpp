#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<vector<int>> graph(n);
    while (m--) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    vector<char> seen(n);
    int components = 0, largest = 0;
    for (int start = 0; start < n; ++start) if (!seen[start]) {
        ++components;
        int size = 0;
        vector<int> stack{start};
        seen[start] = true;
        while (!stack.empty()) {
            int u = stack.back();
            stack.pop_back();
            ++size;
            for (int v : graph[u]) if (!seen[v]) {
                seen[v] = true;
                stack.push_back(v);
            }
        }
        largest = max(largest, size);
    }
    cout << components << ' ' << components - 1 << ' ' << largest << '\n';
}
