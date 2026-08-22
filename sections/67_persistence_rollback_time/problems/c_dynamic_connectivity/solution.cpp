#include <bits/stdc++.h>
using namespace std;
struct DSU {
  vector<int> parent, size;
  vector<pair<int, int>> history;
  DSU(int n) : parent(n), size(n, 1) { iota(parent.begin(), parent.end(), 0); }
  int find(int x) {
    while (x != parent[x]) x = parent[x];
    return x;
  }
  int snapshot() { return history.size(); }
  void join(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return;
    if (size[a] < size[b]) swap(a, b);
    history.push_back({b, size[a]});
    parent[b] = a;
    size[a] += size[b];
  }
  void rollback(int snap) {
    while ((int)history.size() > snap) {
      auto [b, old] = history.back();
      history.pop_back();
      int a = parent[b];
      size[a] = old;
      parent[b] = b;
    }
  }
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
  map<pair<int, int>, int> opened;
  vector<vector<pair<int, int>>> seg(4 * q + 4);
  function<void(int, int, int, int, int, pair<int, int>)> add =
      [&](int node, int lo, int hi, int ql, int qr, pair<int, int> e) {
        if (ql >= hi || qr <= lo) return;
        if (ql <= lo && hi <= qr) {
          seg[node].push_back(e);
          return;
        }
        int mid = (lo + hi) / 2;
        add(node * 2, lo, mid, ql, qr, e);
        add(node * 2 + 1, mid, hi, ql, qr, e);
      };
  for (int t = 0; t < q; t++) {
    cin >> ops[t].type >> ops[t].u >> ops[t].v;
    --ops[t].u;
    --ops[t].v;
    if (ops[t].u > ops[t].v) swap(ops[t].u, ops[t].v);
    auto e = pair{ops[t].u, ops[t].v};
    if (ops[t].type == '+')
      opened[e] = t;
    else if (ops[t].type == '-') {
      add(1, 0, q, opened[e], t, e);
      opened.erase(e);
    }
  }
  for (auto [e, start] : opened) add(1, 0, q, start, q, e);
  DSU dsu(n);
  function<void(int, int, int)> dfs = [&](int node, int lo, int hi) {
    int snap = dsu.snapshot();
    for (auto [u, v] : seg[node]) dsu.join(u, v);
    if (hi - lo == 1) {
      if (ops[lo].type == '?')
        cout << (dsu.find(ops[lo].u) == dsu.find(ops[lo].v) ? "YES\n" : "NO\n");
    } else {
      int mid = (lo + hi) / 2;
      dfs(node * 2, lo, mid);
      dfs(node * 2 + 1, mid, hi);
    }
    dsu.rollback(snap);
  };
  if (q) dfs(1, 0, q);
}
