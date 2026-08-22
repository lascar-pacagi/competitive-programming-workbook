#include <bits/stdc++.h>
using namespace std;

constexpr int MOD = 1'000'000'007;

struct Constraint {
    int u, v, parity;
};

class RollbackParityDSU {
    struct Change {
        int type;
        int child = -1;
        int root = -1;
        int root_size = 0;
        int child_size = 0;
        int child_parity = 0;
    };

    vector<int> parent;
    vector<int> parity_to_parent;
    vector<Change> history;

public:
    int components;
    int contradictions = 0;

    explicit RollbackParityDSU(int n)
        : parent(n, -1), parity_to_parent(n), components(n) {}

    pair<int, int> find(int x) const {
        int parity = 0;
        while (parent[x] >= 0) {
            parity ^= parity_to_parent[x];
            x = parent[x];
        }
        return {x, parity};
    }

    int snapshot() const { return static_cast<int>(history.size()); }

    void add(int u, int v, int required) {
        auto [root_u, parity_u] = find(u);
        auto [root_v, parity_v] = find(v);
        if (root_u == root_v) {
            if ((parity_u ^ parity_v) != required) {
                ++contradictions;
                history.push_back({1});
            } else {
                history.push_back({0});
            }
            return;
        }
        if (-parent[root_u] < -parent[root_v]) {
            swap(root_u, root_v);
            swap(parity_u, parity_v);
        }
        history.push_back({2, root_v, root_u, parent[root_u], parent[root_v],
                           parity_to_parent[root_v]});
        parent[root_u] += parent[root_v];
        parent[root_v] = root_u;
        parity_to_parent[root_v] = parity_u ^ parity_v ^ required;
        --components;
    }

    void rollback(int target) {
        while (static_cast<int>(history.size()) > target) {
            Change change = history.back();
            history.pop_back();
            if (change.type == 1) {
                --contradictions;
            } else if (change.type == 2) {
                parent[change.root] = change.root_size;
                parent[change.child] = change.child_size;
                parity_to_parent[change.child] = change.child_parity;
                ++components;
            }
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;
    vector<vector<Constraint>> timeline(4 * q + 4);
    vector<bool> is_query(q);
    vector<int> start(q, -1);
    vector<Constraint> inserted(q);

    auto add_interval = [&](auto &&self, int node, int left, int right,
                            int query_left, int query_right,
                            Constraint constraint) -> void {
        if (query_right <= left || right <= query_left) return;
        if (query_left <= left && right <= query_right) {
            timeline[node].push_back(constraint);
            return;
        }
        int middle = (left + right) / 2;
        self(self, node * 2, left, middle, query_left, query_right, constraint);
        self(self, node * 2 + 1, middle, right, query_left, query_right, constraint);
    };

    for (int time = 0; time < q; ++time) {
        char type;
        cin >> type;
        if (type == '+') {
            int u, v, parity;
            cin >> u >> v >> parity;
            inserted[time] = {u - 1, v - 1, parity};
            start[time] = time;
        } else if (type == '-') {
            int identifier;
            cin >> identifier;
            --identifier;
            add_interval(add_interval, 1, 0, q, start[identifier], time,
                         inserted[identifier]);
            start[identifier] = -1;
        } else {
            is_query[time] = true;
        }
    }
    for (int identifier = 0; identifier < q; ++identifier)
        if (start[identifier] != -1)
            add_interval(add_interval, 1, 0, q, start[identifier], q,
                         inserted[identifier]);

    vector<int> powers(n + 1, 1);
    for (int i = 1; i <= n; ++i)
        powers[i] = static_cast<long long>(powers[i - 1]) * 2 % MOD;

    RollbackParityDSU dsu(n);
    auto solve = [&](auto &&self, int node, int left, int right) -> void {
        int saved = dsu.snapshot();
        for (Constraint constraint : timeline[node])
            dsu.add(constraint.u, constraint.v, constraint.parity);
        if (right - left == 1) {
            if (is_query[left])
                cout << (dsu.contradictions ? 0 : powers[dsu.components]) << '\n';
        } else {
            int middle = (left + right) / 2;
            self(self, node * 2, left, middle);
            self(self, node * 2 + 1, middle, right);
        }
        dsu.rollback(saved);
    };
    solve(solve, 1, 0, q);
}
