#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct Seg {
  int n;
  vector<ll> mx, lz;
  Seg(vector<ll> &a) {
    n = a.size();
    mx.resize(4 * n);
    lz.resize(4 * n);
    function<void(int, int, int)> b = [&](int x, int l, int r) {
      if (r - l == 1) {
        mx[x] = a[l];
        return;
      }
      int m = (l + r) / 2;
      b(2 * x, l, m);
      b(2 * x + 1, m, r);
      mx[x] = max(mx[2 * x], mx[2 * x + 1]);
    };
    b(1, 0, n);
  }
  void add(int x, int l, int r, int ql, int qr, ll v) {
    if (ql >= r || qr <= l)
      return;
    if (ql <= l && r <= qr) {
      mx[x] += v;
      lz[x] += v;
      return;
    }
    int m = (l + r) / 2;
    add(2 * x, l, m, ql, qr, v);
    add(2 * x + 1, m, r, ql, qr, v);
    mx[x] = lz[x] + max(mx[2 * x], mx[2 * x + 1]);
  }
  ll get(int x, int l, int r, int ql, int qr, ll carry = 0) {
    if (ql >= r || qr <= l)
      return LLONG_MIN;
    if (ql <= l && r <= qr)
      return mx[x] + carry;
    int m = (l + r) / 2;
    return max(get(2 * x, l, m, ql, qr, carry + lz[x]),
               get(2 * x + 1, m, r, ql, qr, carry + lz[x]));
  }
};
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  if (!(cin >> n >> q))
    return 0;
  vector<ll> a(n);
  for (auto &x : a)
    cin >> x;
  vector<vector<int>> g(n);
  for (int i = 1, u, v; i < n; i++) {
    cin >> u >> v;
    --u;
    --v;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  vector<int> p(n, -1), dep(n), sz(n, 1), heavy(n, -1), head(n), pos(n),
      ord = {0};
  for (int i = 0; i < (int)ord.size(); i++) {
    int u = ord[i];
    for (int v : g[u])
      if (v != p[u])
        p[v] = u, dep[v] = dep[u] + 1, ord.push_back(v);
  }
  for (int z = n - 1; z; z--) {
    int u = ord[z];
    sz[p[u]] += sz[u];
    if (heavy[p[u]] < 0 || sz[u] > sz[heavy[p[u]]])
      heavy[p[u]] = u;
  }
  int timer = 0;
  vector<pair<int, int>> todo = {{0, 0}};
  while (!todo.empty()) {
    auto [u, h] = todo.back();
    todo.pop_back();
    for (int x = u; x != -1; x = heavy[x]) {
      head[x] = h;
      pos[x] = timer++;
      for (int v : g[x])
        if (v != p[x] && v != heavy[x])
          todo.push_back({v, v});
    }
  }
  vector<ll> flat(n);
  for (int u = 0; u < n; u++)
    flat[pos[u]] = a[u];
  Seg s(flat);
  auto each = [&](int u, int v, auto f) {
    while (head[u] != head[v]) {
      if (dep[head[u]] < dep[head[v]])
        swap(u, v);
      f(pos[head[u]], pos[u] + 1);
      u = p[head[u]];
    }
    if (dep[u] > dep[v])
      swap(u, v);
    f(pos[u], pos[v] + 1);
  };
  while (q--) {
    char c;
    int u, v;
    cin >> c >> u >> v;
    --u;
    --v;
    if (c == 'A') {
      ll x;
      cin >> x;
      each(u, v, [&](int l, int r) { s.add(1, 0, n, l, r, x); });
    } else {
      ll ans = LLONG_MIN;
      each(u, v, [&](int l, int r) { ans = max(ans, s.get(1, 0, n, l, r)); });
      cout << ans << '\n';
    }
  }
}
