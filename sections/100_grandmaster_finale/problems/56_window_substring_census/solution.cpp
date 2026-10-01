#include <bits/stdc++.h>
using namespace std;

// Count each distinct substring of s[l..r] at its LAST occurrence ending at or
// before r; it is inside the window iff that occurrence starts at >= l.
// Sweep r.  In the suffix automaton, the suffixes of s[1..r] are the states on
// the suffix-link path from the prefix state to the root, and a state's
// substrings share their last end position.  A link-cut tree over the
// suffix-link tree keeps every preferred path uniformly coloured by that last
// end e: a coloured chain top..x covers lengths (len(link(top)), len(x)], i.e.
// start positions [e - len(x) + 1, e - len(link(top))].  Accessing the prefix
// state recolours its root path with r, removing the old chains' starts from a
// range-add/range-sum Fenwick tree and adding starts [1, r].

typedef long long ll;

struct Fenwick {  // range add, range sum over positions 1..n
    int n;
    vector<ll> a, b;
    Fenwick(int n) : n(n), a(n + 2, 0), b(n + 2, 0) {}
    void addPoint(vector<ll>& t, int i, ll v) {
        for (; i <= n + 1; i += i & -i) t[i] += v;
    }
    void rangeAdd(int l, int r, ll v) {  // add v to [l, r]
        if (l > r) return;
        addPoint(a, l, v);
        addPoint(a, r + 1, -v);
        addPoint(b, l, v * (l - 1));
        addPoint(b, r + 1, -v * r);
    }
    ll prefix(int i) {
        ll sa = 0, sb = 0;
        for (int k = i; k > 0; k -= k & -k) sa += a[k], sb += b[k];
        return sa * i - sb;
    }
    ll rangeSum(int l, int r) { return prefix(r) - prefix(l - 1); }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    int q;
    cin >> s >> q;
    int n = s.size();
    // Suffix automaton.
    vector<int> len(2 * n + 1, 0), link(2 * n + 1, -1), prefixState(n + 1);
    vector<array<int, 26>> nxt(2 * n + 1);
    for (auto& row : nxt) row.fill(-1);
    int states = 1, last = 0;
    for (int i = 0; i < n; i++) {
        int c = s[i] - 'a', cur = states++;
        len[cur] = len[last] + 1;
        int p = last;
        while (p != -1 && nxt[p][c] == -1) nxt[p][c] = cur, p = link[p];
        if (p == -1) {
            link[cur] = 0;
        } else {
            int qq = nxt[p][c];
            if (len[p] + 1 == len[qq]) {
                link[cur] = qq;
            } else {
                int clone = states++;
                len[clone] = len[p] + 1;
                nxt[clone] = nxt[qq];
                link[clone] = link[qq];
                while (p != -1 && nxt[p][c] == qq) nxt[p][c] = clone, p = link[p];
                link[qq] = link[cur] = clone;
            }
        }
        last = cur;
        prefixState[i + 1] = cur;
    }
    nxt.clear();
    nxt.shrink_to_fit();

    // Link-cut tree over the suffix-link tree (rooted, no reversal needed).
    // Node ids are state + 1 so that 0 is the null node.
    int N = states + 1;
    vector<int> ch0(N, 0), ch1(N, 0), fa(N, 0), colour(N, 0), tag(N, 0), leftmost(N);
    for (int v = 1; v < N; v++) {
        leftmost[v] = v;
        fa[v] = link[v - 1] >= 0 ? link[v - 1] + 1 : 0;
    }
    auto isRoot = [&](int x) { return !fa[x] || (ch0[fa[x]] != x && ch1[fa[x]] != x); };
    auto pull = [&](int x) { leftmost[x] = ch0[x] ? leftmost[ch0[x]] : x; };
    auto apply = [&](int x, int c) {
        if (x) colour[x] = tag[x] = c;
    };
    auto push = [&](int x) {
        if (tag[x]) {
            apply(ch0[x], tag[x]);
            apply(ch1[x], tag[x]);
            tag[x] = 0;
        }
    };
    auto rotate = [&](int x) {
        int p = fa[x], g = fa[p];
        bool right = ch1[p] == x;
        if (!isRoot(p)) (ch0[g] == p ? ch0[g] : ch1[g]) = x;
        fa[x] = g;
        if (right) {
            ch1[p] = ch0[x];
            if (ch0[x]) fa[ch0[x]] = p;
            ch0[x] = p;
        } else {
            ch0[p] = ch1[x];
            if (ch1[x]) fa[ch1[x]] = p;
            ch1[x] = p;
        }
        fa[p] = x;
        pull(p);
        pull(x);
    };
    vector<int> path;
    auto splay = [&](int x) {
        path.clear();
        for (int y = x;; y = fa[y]) {
            path.push_back(y);
            if (isRoot(y)) break;
        }
        for (int i = (int)path.size() - 1; i >= 0; i--) push(path[i]);
        while (!isRoot(x)) {
            int p = fa[x], g = fa[p];
            if (!isRoot(p)) rotate((ch0[g] == p) == (ch0[p] == x) ? p : x);
            rotate(x);
        }
    };
    Fenwick fen(n);
    auto access = [&](int x, int r) {
        int start = x;
        for (int y = 0; x; y = x, x = fa[x]) {
            splay(x);
            int c = colour[x];
            if (c) {
                int top = ch0[x] ? leftmost[ch0[x]] : x;
                int lowLen = link[top - 1] >= 0 ? len[link[top - 1]] : 0;
                fen.rangeAdd(c - len[x - 1] + 1, c - lowLen, -1);
            }
            ch1[x] = y;
            pull(x);
        }
        splay(start);
        apply(start, r);
        fen.rangeAdd(1, r, 1);  // the whole root path: lengths 1..r ending at r
    };

    vector<int> ql(q), qr(q), order(q);
    for (int i = 0; i < q; i++) cin >> ql[i] >> qr[i];
    iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(), [&](int a, int b) { return qr[a] < qr[b]; });
    vector<ll> answer(q);
    int done = 0;
    for (int id : order) {
        while (done < qr[id]) {
            done++;
            access(prefixState[done] + 1, done);
        }
        answer[id] = fen.rangeSum(ql[id], qr[id]);
    }
    string out;
    for (ll x : answer) out += to_string(x) + '\n';
    cout << out;
}
