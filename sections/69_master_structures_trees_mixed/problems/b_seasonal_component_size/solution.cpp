#include <bits/stdc++.h>
using namespace std;
struct DSU {
  vector<int> p, s;
  vector<pair<int, int>> h;
  DSU(int n) : p(n), s(n, 1) { iota(p.begin(), p.end(), 0); }
  int find(int x) {
    while (x != p[x]) x = p[x];
    return x;
  }
  int snap() { return h.size(); }
  void join(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return;
    if (s[a] < s[b]) swap(a, b);
    h.push_back({b, s[a]});
    p[b] = a;
    s[a] += s[b];
  }
  void rollback(int z) {
    while ((int)h.size() > z) {
      auto [b, old] = h.back();
      h.pop_back();
      int a = p[b];
      s[a] = old;
      p[b] = b;
    }
  }
  int component(int x) { return s[find(x)]; }
};
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  if (!(cin >> n >> q)) return 0;
  struct Op {
    char type;
    int u, v;
  };
  vector<Op> ops(q);
  map<pair<int, int>, int> open;
  vector<vector<pair<int, int>>> seg(4 * q + 4);
  function<void(int, int, int, int, int, pair<int, int>)> add =
      [&](int x, int l, int r, int ql, int qr, pair<int, int> e) {
        if (ql >= r || qr <= l) return;
        if (ql <= l && r <= qr) {
          seg[x].push_back(e);
          return;
        }
        int m = (l + r) / 2;
        add(2 * x, l, m, ql, qr, e);
        add(2 * x + 1, m, r, ql, qr, e);
      };
  for (int t = 0; t < q; t++) {
    cin >> ops[t].type >> ops[t].u;
    --ops[t].u;
    ops[t].v = -1;
    if (ops[t].type != 'S') {
      cin >> ops[t].v;
      --ops[t].v;
      if (ops[t].u > ops[t].v) swap(ops[t].u, ops[t].v);
      auto e = pair{ops[t].u, ops[t].v};
      if (ops[t].type == '+')
        open[e] = t;
      else
        add(1, 0, q, open[e], t, e), open.erase(e);
    }
  }
  for (auto [e, t] : open) add(1, 0, q, t, q, e);
  DSU dsu(n);
  function<void(int, int, int)> dfs = [&](int x, int l, int r) {
    int z = dsu.snap();
    for (auto [u, v] : seg[x]) dsu.join(u, v);
    if (r - l == 1) {
      if (ops[l].type == 'S') cout << dsu.component(ops[l].u) << '\n';
    } else {
      int m = (l + r) / 2;
      dfs(2 * x, l, m);
      dfs(2 * x + 1, m, r);
    }
    dsu.rollback(z);
  };
  if (q) dfs(1, 0, q);
}
