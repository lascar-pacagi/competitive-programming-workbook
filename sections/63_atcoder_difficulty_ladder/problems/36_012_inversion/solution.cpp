#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<vector<int>> graph(n);
    for (int edge = 0; edge + 1 < n; ++edge) {
        int left, right;
        cin >> left >> right;
        --left;
        --right;
        graph[left].push_back(right);
        graph[right].push_back(left);
    }

    vector<int> parent(n, -1), order{0};
    for (int index = 0; index < (int)order.size(); ++index) {
        int vertex = order[index];
        for (int neighbor : graph[vertex]) {
            if (neighbor != parent[vertex]) {
                parent[neighbor] = vertex;
                order.push_back(neighbor);
            }
        }
    }

    vector<int> down_without(n), down_with(n, 1);
    for (int index = n - 1; index >= 0; --index) {
        int vertex = order[index];
        for (int child : graph[vertex]) {
            if (parent[child] == vertex) {
                down_without[vertex] += max(down_without[child], down_with[child]);
                down_with[vertex] += down_without[child];
            }
        }
    }

    vector<int> outside_without(n), outside_with(n), answer(n);
    for (int vertex : order) {
        answer[vertex] = down_with[vertex] + outside_with[vertex];
        for (int child : graph[vertex]) {
            if (parent[child] != vertex) continue;
            int siblings_free = down_without[vertex] - max(down_without[child], down_with[child]);
            int siblings_without = down_with[vertex] - 1 - down_without[child];
            outside_with[child] = outside_without[vertex] + siblings_free;
            outside_without[child] = max(
                outside_without[vertex] + siblings_free,
                outside_with[vertex] + 1 + siblings_without
            );
        }
    }

    for (int vertex = 0; vertex < n; ++vertex) {
        cout << answer[vertex] << (vertex + 1 == n ? '\n' : ' ');
    }
}
