#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

constexpr int64 INF = 4'000'000'000'000'000'000LL;
using State = pair<int64, int>;

State add_state(State a, State b) {
    if (a.first >= INF || b.first >= INF) return {INF, INT_MAX / 2};
    return {a.first + b.first, a.second + b.second};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, query_count;
    cin >> n >> query_count;
    vector<vector<pair<int, int64>>> graph(n);
    for (int i = 1; i < n; ++i) {
        int u, v;
        int64 cost;
        cin >> u >> v >> cost;
        --u;
        --v;
        graph[u].push_back({v, cost});
        graph[v].push_back({u, cost});
    }

    int log = max(1, static_cast<int>(bit_width(static_cast<unsigned>(n))));
    vector<vector<int>> up(log, vector<int>(n));
    vector<vector<int64>> minimum(log, vector<int64>(n, INF));
    vector<int> depth(n), tin(n), tout(n);
    struct Event { int u, parent; int64 weight; bool exit; };
    vector<Event> events{{0, 0, INF, false}};
    int timer = 0;
    while (!events.empty()) {
        Event event = events.back();
        events.pop_back();
        int u = event.u;
        if (event.exit) {
            tout[u] = timer;
            continue;
        }
        tin[u] = timer++;
        up[0][u] = event.parent;
        minimum[0][u] = event.weight;
        if (u != 0) depth[u] = depth[event.parent] + 1;
        for (int bit = 1; bit < log; ++bit) {
            up[bit][u] = up[bit - 1][up[bit - 1][u]];
            minimum[bit][u] = min(minimum[bit - 1][u],
                                  minimum[bit - 1][up[bit - 1][u]]);
        }
        events.push_back({u, event.parent, event.weight, true});
        for (auto it = graph[u].rbegin(); it != graph[u].rend(); ++it)
            if (it->first != event.parent)
                events.push_back({it->first, u, it->second, false});
    }

    auto is_ancestor = [&](int u, int v) {
        return tin[u] <= tin[v] && tout[v] <= tout[u];
    };
    auto lca = [&](int u, int v) {
        if (is_ancestor(u, v)) return u;
        if (is_ancestor(v, u)) return v;
        for (int bit = log - 1; bit >= 0; --bit)
            if (!is_ancestor(up[bit][u], v)) u = up[bit][u];
        return up[0][u];
    };
    auto path_minimum = [&](int ancestor, int vertex) {
        int difference = depth[vertex] - depth[ancestor];
        int64 result = INF;
        for (int bit = 0; bit < log; ++bit) {
            if (difference >> bit & 1) {
                result = min(result, minimum[bit][vertex]);
                vertex = up[bit][vertex];
            }
        }
        return result;
    };

    vector<int> marked(n);
    int token = 0;
    while (query_count--) {
        int k;
        cin >> k;
        vector<int> terminals(k);
        ++token;
        for (int &v : terminals) {
            cin >> v;
            --v;
            marked[v] = token;
        }
        if (k <= 1) {
            cout << "0 0\n";
            continue;
        }
        sort(terminals.begin(), terminals.end(),
             [&](int u, int v) { return tin[u] < tin[v]; });
        vector<int> nodes = terminals;
        for (int i = 1; i < k; ++i) nodes.push_back(lca(terminals[i - 1], terminals[i]));
        sort(nodes.begin(), nodes.end(), [&](int u, int v) { return tin[u] < tin[v]; });
        nodes.erase(unique(nodes.begin(), nodes.end()), nodes.end());

        vector<vector<pair<int, int64>>> virtual_children(nodes.size());
        vector<int> stack;
        for (int i = 0; i < static_cast<int>(nodes.size()); ++i) {
            while (!stack.empty() && !is_ancestor(nodes[stack.back()], nodes[i]))
                stack.pop_back();
            if (!stack.empty()) {
                int parent_index = stack.back();
                virtual_children[parent_index].push_back(
                    {i, path_minimum(nodes[parent_index], nodes[i])});
            }
            stack.push_back(i);
        }

        vector<State> dp_zero(nodes.size()), dp_one(nodes.size());
        for (int i = static_cast<int>(nodes.size()) - 1; i >= 0; --i) {
            State zero = marked[nodes[i]] == token ? State{INF, INT_MAX / 2}
                                                    : State{0, 0};
            State one = marked[nodes[i]] == token ? State{0, 0}
                                                   : State{INF, INT_MAX / 2};
            for (auto [child, edge_cost] : virtual_children[i]) {
                State separated = min(dp_zero[child],
                                      add_state(dp_one[child], {edge_cost, 1}));
                State new_zero = add_state(zero, separated);
                State new_one = min(add_state(one, separated),
                                    add_state(zero, dp_one[child]));
                zero = new_zero;
                one = new_one;
            }
            dp_zero[i] = zero;
            dp_one[i] = one;
        }
        State answer = min(dp_zero[0], dp_one[0]);
        cout << answer.first << ' ' << answer.second << '\n';
    }
}
