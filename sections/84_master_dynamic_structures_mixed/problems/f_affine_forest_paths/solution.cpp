#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct LCT {
  int n, mode;
  ll mod;
  vector<array<int, 2>> ch;
  vector<int> p, rev, sz;
  vector<ll> val, agg, mul, add;
  LCT(vector<ll> a, int mode = 0, ll mod = 0)
      : n(a.size()), mode(mode), mod(mod), ch(n + 1), p(n + 1), rev(n + 1),
        sz(n + 1, 1), val(n + 1), agg(n + 1), mul(n + 1, 1), add(n + 1) {
    sz[0] = 0;
    for (int i = 1; i <= n; i++)
      val[i] = agg[i] = a[i - 1];
  }
  bool root(int x) { return !p[x] || (ch[p[x]][0] != x && ch[p[x]][1] != x); }
  void pull(int x) {
    auto [l, r] = ch[x];
    sz[x] = 1 + sz[l] + sz[r];
    agg[x] = mode ? (agg[l] ^ val[x] ^ agg[r]) : agg[l] + val[x] + agg[r];
    if (mod)
      agg[x] %= mod;
  }
  void reverse_node(int x) {
    if (x)
      swap(ch[x][0], ch[x][1]), rev[x] ^= 1;
  }
  void affine(int x, ll a, ll b) {
    if (!x)
      return;
    val[x] = (a * val[x] + b) % mod;
    agg[x] = (a * agg[x] + b * sz[x]) % mod;
    mul[x] = a * mul[x] % mod;
    add[x] = (a * add[x] + b) % mod;
  }
  void push(int x) {
    if (rev[x])
      reverse_node(ch[x][0]), reverse_node(ch[x][1]), rev[x] = 0;
    if (mul[x] != 1 || add[x]) {
      affine(ch[x][0], mul[x], add[x]);
      affine(ch[x][1], mul[x], add[x]);
      mul[x] = 1;
      add[x] = 0;
    }
  }
  void rotate(int x) {
    int y = p[x], z = p[y], s = ch[y][1] == x, b = ch[x][s ^ 1];
    if (!root(y))
      ch[z][ch[z][1] == y] = x;
    p[x] = z;
    ch[x][s ^ 1] = y;
    p[y] = x;
    ch[y][s] = b;
    if (b)
      p[b] = y;
    pull(y);
    pull(x);
  }
  void splay(int x) {
    vector<int> st = {x};
    for (int y = x; !root(y);)
      y = p[y], st.push_back(y);
    while (!st.empty())
      push(st.back()), st.pop_back();
    while (!root(x)) {
      int y = p[x], z = p[y];
      if (!root(y))
        rotate((ch[y][1] == x) == (ch[z][1] == y) ? y : x);
      rotate(x);
    }
  }
  void access(int x) {
    for (int y = 0, z = x; z; y = z, z = p[z])
      splay(z), ch[z][1] = y, pull(z);
    splay(x);
  }
  void makeroot(int x) {
    access(x);
    reverse_node(x);
  }
  void link(int x, int y) {
    makeroot(x);
    p[x] = y;
  }
  void cut(int x, int y) {
    makeroot(x);
    access(y);
    ch[y][0] = 0;
    p[x] = 0;
    pull(y);
  }
  int path(int x, int y) {
    makeroot(x);
    access(y);
    return y;
  }
  void setv(int x, ll v) {
    access(x);
    val[x] = v;
    pull(x);
  }
};
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  cin >> n >> q;
  vector<ll> a(n);
  for (auto &x : a)
    cin >> x;
  LCT t(a, 0, 998244353);
  while (q--) {
    string op;
    cin >> op;
    if (op == "LINK") {
      int u, v;
      cin >> u >> v;
      t.link(u, v);
    } else if (op == "CUT") {
      int u, v;
      cin >> u >> v;
      t.cut(u, v);
    } else if (op == "SET") {
      int u;
      ll x;
      cin >> u >> x;
      t.setv(u, x);
    } else if (op == "AFFINE") {
      int u, v;
      ll x, y;
      cin >> u >> v >> x >> y;
      int z = t.path(u, v);
      t.affine(z, x, y);
    } else {
      int u, v;
      cin >> u >> v;
      cout << t.agg[t.path(u, v)] << '\n';
    }
  }
}