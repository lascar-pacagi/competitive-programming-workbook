#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> value(n);
    for (long long &x : value) cin >> x;
    vector<vector<int>> graph(n);
    for (int i = 1; i < n; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<int> parent(n, -1), order{0};
    for (int index = 0; index < n; ++index) {
        int u = order[index];
        for (int v : graph[u]) if (v != parent[u]) {
            parent[v] = u;
            order.push_back(v);
        }
    }

    using MinHeap = priority_queue<long long, vector<long long>, greater<long long>>;
    vector<unique_ptr<MinHeap>> heap(n);
    long long answer = 0;
    for (int index = n - 1; index >= 0; --index) {
        int u = order[index];
        heap[u] = make_unique<MinHeap>();
        for (int v : graph[u]) if (parent[v] == u) {
            if (heap[u]->size() < heap[v]->size()) heap[u].swap(heap[v]);
            while (!heap[v]->empty()) {
                heap[u]->push(heap[v]->top());
                heap[v]->pop();
            }
            heap[v].reset();
        }
        heap[u]->push(value[u]);
        heap[u]->push(value[u]);
        long long first_breakpoint = heap[u]->top();
        heap[u]->pop();
        answer += value[u] - first_breakpoint;
    }
    cout << answer << '\n';
}
