#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

constexpr int64 MOD = 1'000'000'007;

struct LinkCutTree {
    int n;
    vector<array<int, 2>> child;
    vector<int> parent, reversed, size;
    vector<int64> value, sum, lazy_mul, lazy_add;

    explicit LinkCutTree(const vector<int64> &initial)
        : n(initial.size()), child(n + 1), parent(n + 1), reversed(n + 1),
          size(n + 1, 1), value(n + 1), sum(n + 1), lazy_mul(n + 1, 1),
          lazy_add(n + 1) {
        size[0] = 0;
        for (int i = 1; i <= n; ++i) value[i] = sum[i] = initial[i - 1];
    }

    bool is_auxiliary_root(int x) const {
        int p = parent[x];
        return p == 0 || (child[p][0] != x && child[p][1] != x);
    }

    void pull(int x) {
        int left = child[x][0], right = child[x][1];
        size[x] = 1 + size[left] + size[right];
        sum[x] = (sum[left] + value[x] + sum[right]) % MOD;
    }

    void apply_reverse(int x) {
        if (x == 0) return;
        swap(child[x][0], child[x][1]);
        reversed[x] ^= 1;
    }

    void apply_affine(int x, int64 multiplier, int64 addition) {
        if (x == 0) return;
        value[x] = (multiplier * value[x] + addition) % MOD;
        sum[x] = (multiplier * sum[x] + addition * size[x]) % MOD;
        lazy_mul[x] = multiplier * lazy_mul[x] % MOD;
        lazy_add[x] = (multiplier * lazy_add[x] + addition) % MOD;
    }

    void push(int x) {
        if (reversed[x]) {
            apply_reverse(child[x][0]);
            apply_reverse(child[x][1]);
            reversed[x] = 0;
        }
        if (lazy_mul[x] != 1 || lazy_add[x] != 0) {
            apply_affine(child[x][0], lazy_mul[x], lazy_add[x]);
            apply_affine(child[x][1], lazy_mul[x], lazy_add[x]);
            lazy_mul[x] = 1;
            lazy_add[x] = 0;
        }
    }

    void rotate(int x) {
        int p = parent[x], g = parent[p];
        int side = child[p][1] == x;
        int middle = child[x][side ^ 1];
        if (!is_auxiliary_root(p)) child[g][child[g][1] == p] = x;
        parent[x] = g;
        child[x][side ^ 1] = p;
        parent[p] = x;
        child[p][side] = middle;
        if (middle) parent[middle] = p;
        pull(p);
        pull(x);
    }

    void splay(int x) {
        vector<int> ancestors{x};
        for (int y = x; !is_auxiliary_root(y);) {
            y = parent[y];
            ancestors.push_back(y);
        }
        while (!ancestors.empty()) {
            push(ancestors.back());
            ancestors.pop_back();
        }
        while (!is_auxiliary_root(x)) {
            int p = parent[x], g = parent[p];
            if (!is_auxiliary_root(p))
                rotate((child[p][1] == x) == (child[g][1] == p) ? p : x);
            rotate(x);
        }
    }

    void access(int x) {
        int previous = 0;
        for (int current = x; current; current = parent[current]) {
            splay(current);
            child[current][1] = previous;
            pull(current);
            previous = current;
        }
        splay(x);
    }

    void make_root(int x) {
        access(x);
        apply_reverse(x);
    }

    void link(int u, int v) {
        make_root(u);
        parent[u] = v;
    }

    void cut(int u, int v) {
        make_root(u);
        access(v);
        child[v][0] = 0;
        parent[u] = 0;
        pull(v);
    }

    int expose_path(int u, int v) {
        make_root(u);
        access(v);
        return v;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;
    vector<int64> initial(n);
    for (int64 &x : initial) cin >> x;
    LinkCutTree tree(initial);
    while (q--) {
        string operation;
        int u, v;
        cin >> operation >> u >> v;
        if (operation == "LINK") {
            tree.link(u, v);
        } else if (operation == "CUT") {
            tree.cut(u, v);
        } else if (operation == "AFFINE") {
            int64 multiplier, addition;
            cin >> multiplier >> addition;
            tree.apply_affine(tree.expose_path(u, v), multiplier, addition);
        } else {
            cout << tree.sum[tree.expose_path(u, v)] << '\n';
        }
    }
}
