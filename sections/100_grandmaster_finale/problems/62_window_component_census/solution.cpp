#include <bits/stdc++.h>
using namespace std;

// Scan cables in order while keeping the spanning forest that prefers newer
// cables (a link-cut tree over vertex nodes and cable nodes, path minimum of
// cable index).  When cable i closes a cycle, the oldest cable on that cycle
// leaves the forest; call its index pre[i] (pre[i] = 0 when nothing leaves,
// pre[i] = i for a self-loop).  For a window [l, r], cable i in the window
// merges two components of the window graph iff pre[i] < l, so the answer is
// n - #{i in [l, r] : pre[i] < l}, counted offline with a Fenwick tree.

const int INF = INT_MAX;
vector<int> ch[2], par, val, mn;
vector<char> rev;

bool isRoot(int x) { return !par[x] || (ch[0][par[x]] != x && ch[1][par[x]] != x); }
void pull(int x) {
    mn[x] = x;
    for (int d = 0; d < 2; d++)
        if (ch[d][x] && val[mn[ch[d][x]]] < val[mn[x]]) mn[x] = mn[ch[d][x]];
}
void flip(int x) {
    if (x) {
        swap(ch[0][x], ch[1][x]);
        rev[x] ^= 1;
    }
}
void push(int x) {
    if (rev[x]) {
        flip(ch[0][x]);
        flip(ch[1][x]);
        rev[x] = 0;
    }
}
void rotate(int x) {
    int p = par[x], g = par[p];
    int d = ch[1][p] == x;
    if (!isRoot(p)) ch[ch[1][g] == p][g] = x;
    par[x] = g;
    ch[d][p] = ch[!d][x];
    if (ch[!d][x]) par[ch[!d][x]] = p;
    ch[!d][x] = p;
    par[p] = x;
    pull(p);
    pull(x);
}
void splay(int x) {
    static vector<int> path;
    path.clear();
    for (int y = x;; y = par[y]) {
        path.push_back(y);
        if (isRoot(y)) break;
    }
    for (int i = (int)path.size() - 1; i >= 0; i--) push(path[i]);
    while (!isRoot(x)) {
        int p = par[x], g = par[p];
        if (!isRoot(p)) rotate((ch[0][g] == p) == (ch[0][p] == x) ? p : x);
        rotate(x);
    }
}
void access(int x) {
    for (int last = 0; x; last = x, x = par[x]) {
        splay(x);
        ch[1][x] = last;
        pull(x);
    }
}
void makeRoot(int x) {
    access(x);
    splay(x);
    flip(x);
}
int findRoot(int x) {
    access(x);
    splay(x);
    while (true) {
        push(x);
        if (!ch[0][x]) break;
        x = ch[0][x];
    }
    splay(x);
    return x;
}
void link(int x, int y) {
    makeRoot(x);
    par[x] = y;
}
void cut(int x, int y) {
    makeRoot(x);
    access(y);
    splay(y);
    ch[0][y] = 0;
    par[x] = 0;
    pull(y);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, q;
    cin >> n >> m >> q;
    int total = n + m + 1;
    for (auto& c : ch) c.assign(total, 0);
    par.assign(total, 0);
    val.assign(total, INF);
    mn.resize(total);
    rev.assign(total, 0);
    for (int i = 0; i < total; i++) mn[i] = i;
    vector<int> eu(m + 1), ev(m + 1), pre(m + 1, 0);
    for (int i = 1; i <= m; i++) {
        cin >> eu[i] >> ev[i];
        int u = eu[i], v = ev[i], node = n + i;
        val[node] = i;
        if (u == v) {
            pre[i] = i;
            continue;
        }
        if (findRoot(u) == findRoot(v)) {
            makeRoot(u);
            access(v);
            splay(v);
            int oldest = mn[v];
            int j = oldest - n;
            pre[i] = j;
            cut(eu[j], oldest);
            cut(oldest, ev[j]);
        }
        link(u, node);
        link(node, v);
    }

    // Offline count of i in [l, r] with pre[i] < l: sweep l upward.
    vector<int> ql(q), qr(q), order(q);
    for (int i = 0; i < q; i++) cin >> ql[i] >> qr[i];
    iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(), [&](int a, int b) { return ql[a] < ql[b]; });
    vector<int> byPre(m);
    iota(byPre.begin(), byPre.end(), 1);
    sort(byPre.begin(), byPre.end(), [&](int a, int b) { return pre[a] < pre[b]; });
    vector<int> bit(m + 1, 0);
    vector<int> answer(q);
    size_t ptr = 0;
    for (int id : order) {
        while (ptr < byPre.size() && pre[byPre[ptr]] < ql[id]) {
            for (int k = byPre[ptr]; k <= m; k += k & -k) bit[k]++;
            ptr++;
        }
        auto prefix = [&](int k) {
            int s = 0;
            for (; k > 0; k -= k & -k) s += bit[k];
            return s;
        };
        answer[id] = n - (prefix(qr[id]) - prefix(ql[id] - 1));
    }
    string out;
    for (int x : answer) out += to_string(x) + '\n';
    cout << out;
}
