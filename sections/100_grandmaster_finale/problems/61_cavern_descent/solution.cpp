#include <bits/stdc++.h>
using namespace std;

// dp[v] = min over proper descendants u of a[v] * b[u] + dp[u].
// Each descendant is the line y = b[u] * X + dp[u], queried at X = a[v].
// Every vertex owns a Li Chao tree over X in [-LIM, LIM]; children's trees are
// merged by re-inserting the lines of one tree's nodes into the other.
// Merging is O(n log C) amortized: a line only ever moves downward.

const int LIM = 100000;

struct Node {
    long long k, m;
    int left, right;
};
vector<Node> pool;
vector<int> freeNodes;  // nodes emptied by merges are recycled

long long eval(const Node& nd, long long x) { return nd.k * x + nd.m; }

int newNode(long long k, long long m) {
    if (!freeNodes.empty()) {
        int t = freeNodes.back();
        freeNodes.pop_back();
        pool[t] = {k, m, 0, 0};
        return t;
    }
    pool.push_back({k, m, 0, 0});
    return pool.size() - 1;
}

// Insert line (k, m) into the subtree rooted at t covering [lo, hi].
int insertLine(int t, int lo, int hi, long long k, long long m) {
    if (!t) return newNode(k, m);
    int root = t;
    while (true) {
        int mid = (lo + hi) >> 1;  // arithmetic shift: floor division
        bool leftBetter = k * lo + m < eval(pool[t], lo);
        bool midBetter = k * mid + m < eval(pool[t], mid);
        if (midBetter) {
            swap(pool[t].k, k);
            swap(pool[t].m, m);
        }
        if (lo == hi) break;
        if (leftBetter != midBetter) {
            if (!pool[t].left) {
                int c = newNode(k, m);
                pool[t].left = c;
                break;
            }
            t = pool[t].left;
            hi = mid;
        } else {
            if (!pool[t].right) {
                int c = newNode(k, m);
                pool[t].right = c;
                break;
            }
            t = pool[t].right;
            lo = mid + 1;
        }
    }
    return root;
}

int mergeTrees(int a, int b, int lo, int hi) {
    if (!a || !b) return a ^ b;
    a = insertLine(a, lo, hi, pool[b].k, pool[b].m);
    int bl = pool[b].left, br = pool[b].right;
    freeNodes.push_back(b);
    if (lo == hi) return a;
    int mid = (lo + hi) >> 1;  // arithmetic shift: floor division
    int nl = mergeTrees(pool[a].left, bl, lo, mid);
    pool[a].left = nl;
    int nr = mergeTrees(pool[a].right, br, mid + 1, hi);
    pool[a].right = nr;
    return a;
}

long long query(int t, long long x) {
    long long best = LLONG_MAX;
    int lo = -LIM, hi = LIM;
    while (t) {
        best = min(best, eval(pool[t], x));
        int mid = (lo + hi) >> 1;
        if (x <= mid) t = pool[t].left, hi = mid;
        else t = pool[t].right, lo = mid + 1;
    }
    return best;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> a(n), b(n);
    for (auto& v : a) cin >> v;
    for (auto& v : b) cin >> v;
    vector<vector<int>> adj(n);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    pool.reserve(n + 1);
    pool.push_back({0, 0, 0, 0});  // node 0 is the null sentinel
    vector<int> order, parent(n, -1);
    order.reserve(n);
    vector<int> stack = {0};
    parent[0] = 0;
    while (!stack.empty()) {
        int v = stack.back();
        stack.pop_back();
        order.push_back(v);
        for (int w : adj[v])
            if (parent[w] < 0) parent[w] = v, stack.push_back(w);
    }
    vector<int> tree(n, 0);
    vector<long long> dp(n, 0);
    for (int i = n - 1; i >= 0; i--) {
        int v = order[i];
        dp[v] = tree[v] ? query(tree[v], a[v]) : 0;
        tree[v] = insertLine(tree[v], -LIM, LIM, b[v], dp[v]);
        if (v) tree[parent[v]] = mergeTrees(tree[parent[v]], tree[v], -LIM, LIM);
    }
    string out;
    for (int i = 0; i < n; i++) {
        out += to_string(dp[i]);
        out += i + 1 < n ? ' ' : '\n';
    }
    cout << out;
}
