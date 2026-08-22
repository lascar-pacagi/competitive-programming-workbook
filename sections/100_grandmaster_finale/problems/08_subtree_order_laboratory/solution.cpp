#include <bits/stdc++.h>
using namespace std;

struct Operation {
    char type;
    int vertex;
    int argument;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;
    vector<int> current(n), all_values;
    vector<vector<int>> possible(n);
    for (int v = 0; v < n; ++v) {
        cin >> current[v];
        possible[v].push_back(current[v]);
        all_values.push_back(current[v]);
    }
    vector<vector<int>> graph(n);
    for (int i = 1; i < n; ++i) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<int> parent(n, -1), order, stack{0};
    while (!stack.empty()) {
        int u = stack.back();
        stack.pop_back();
        order.push_back(u);
        for (auto it = graph[u].rbegin(); it != graph[u].rend(); ++it) {
            int v = *it;
            if (v == parent[u]) continue;
            parent[v] = u;
            stack.push_back(v);
        }
    }
    vector<int> tin(n), subtree_size(n, 1), tout(n);
    for (int i = 0; i < n; ++i) tin[order[i]] = i;
    for (int i = n - 1; i > 0; --i)
        subtree_size[parent[order[i]]] += subtree_size[order[i]];
    for (int v = 0; v < n; ++v) tout[v] = tin[v] + subtree_size[v];

    vector<Operation> operations;
    operations.reserve(q);
    for (int i = 0; i < q; ++i) {
        char type;
        int vertex, argument;
        cin >> type >> vertex >> argument;
        --vertex;
        operations.push_back({type, vertex, argument});
        if (type == 'U') {
            possible[vertex].push_back(argument);
            all_values.push_back(argument);
        }
    }
    sort(all_values.begin(), all_values.end());
    all_values.erase(unique(all_values.begin(), all_values.end()), all_values.end());

    vector<vector<int>> candidates(n + 1);
    for (int v = 0; v < n; ++v) {
        sort(possible[v].begin(), possible[v].end());
        possible[v].erase(unique(possible[v].begin(), possible[v].end()),
                          possible[v].end());
        for (int value : possible[v])
            for (int outer = tin[v] + 1; outer <= n; outer += outer & -outer)
                candidates[outer].push_back(value);
    }
    vector<vector<int>> counts(n + 1);
    for (int outer = 1; outer <= n; ++outer) {
        auto &bucket = candidates[outer];
        sort(bucket.begin(), bucket.end());
        bucket.erase(unique(bucket.begin(), bucket.end()), bucket.end());
        counts[outer].assign(bucket.size() + 1, 0);
    }

    auto modify = [&](int vertex, int value, int delta) {
        for (int outer = tin[vertex] + 1; outer <= n; outer += outer & -outer) {
            int inner = lower_bound(candidates[outer].begin(), candidates[outer].end(),
                                    value) - candidates[outer].begin() + 1;
            for (; inner < static_cast<int>(counts[outer].size()); inner += inner & -inner)
                counts[outer][inner] += delta;
        }
    };
    auto prefix_count = [&](int position, int value) {
        int result = 0;
        for (int outer = position; outer > 0; outer -= outer & -outer) {
            int inner = upper_bound(candidates[outer].begin(), candidates[outer].end(),
                                    value) - candidates[outer].begin();
            for (; inner > 0; inner -= inner & -inner)
                result += counts[outer][inner];
        }
        return result;
    };
    for (int v = 0; v < n; ++v) modify(v, current[v], 1);

    for (Operation operation : operations) {
        int v = operation.vertex;
        if (operation.type == 'U') {
            modify(v, current[v], -1);
            current[v] = operation.argument;
            modify(v, current[v], 1);
        } else {
            int k = operation.argument;
            int left = 0, right = all_values.size() - 1;
            while (left < right) {
                int middle = (left + right) / 2;
                int count = prefix_count(tout[v], all_values[middle])
                          - prefix_count(tin[v], all_values[middle]);
                if (count >= k) right = middle;
                else left = middle + 1;
            }
            cout << all_values[left] << '\n';
        }
    }
}
