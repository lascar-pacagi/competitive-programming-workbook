#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF = 4e18;
struct Beats {
  struct N {
    ll sum = 0, mx = -INF, smx = -INF, mn = INF, smn = INF;
    int mxc = 0, mnc = 0;
  };
  int n;
  vector<N> t;
  Beats(vector<ll> a) : n(a.size()), t(4 * n) { build(1, 0, n, a); }
  void build(int p, int l, int r, vector<ll> &a) {
    if (r - l == 1) {
      t[p] = {a[l], a[l], -INF, a[l], INF, 1, 1};
      return;
    }
    int m = (l + r) / 2;
    build(p * 2, l, m, a);
    build(p * 2 + 1, m, r, a);
    pull(p);
  }
  void pull(int p) {
    N &a = t[p * 2], &b = t[p * 2 + 1], &x = t[p];
    x.sum = a.sum + b.sum;
    if (a.mx > b.mx)
      x.mx = a.mx, x.mxc = a.mxc, x.smx = max(a.smx, b.mx);
    else if (a.mx < b.mx)
      x.mx = b.mx, x.mxc = b.mxc, x.smx = max(a.mx, b.smx);
    else
      x.mx = a.mx, x.mxc = a.mxc + b.mxc, x.smx = max(a.smx, b.smx);
    if (a.mn < b.mn)
      x.mn = a.mn, x.mnc = a.mnc, x.smn = min(a.smn, b.mn);
    else if (a.mn > b.mn)
      x.mn = b.mn, x.mnc = b.mnc, x.smn = min(a.mn, b.smn);
    else
      x.mn = a.mn, x.mnc = a.mnc + b.mnc, x.smn = min(a.smn, b.smn);
  }
  void upper_node(int p, ll x) {
    if (t[p].mx <= x)
      return;
    t[p].sum += (x - t[p].mx) * t[p].mxc;
    if (t[p].mn == t[p].mx)
      t[p].mn = x;
    else if (t[p].smn == t[p].mx)
      t[p].smn = x;
    t[p].mx = x;
  }
  void lower_node(int p, ll x) {
    if (t[p].mn >= x)
      return;
    t[p].sum += (x - t[p].mn) * t[p].mnc;
    if (t[p].mx == t[p].mn)
      t[p].mx = x;
    else if (t[p].smx == t[p].mn)
      t[p].smx = x;
    t[p].mn = x;
  }
  void push(int p) {
    upper_node(p * 2, t[p].mx);
    upper_node(p * 2 + 1, t[p].mx);
    lower_node(p * 2, t[p].mn);
    lower_node(p * 2 + 1, t[p].mn);
  }
  void upper(int ql, int qr, ll x, int p = 1, int l = 0, int r = -1) {
    if (r < 0)
      r = n;
    if (qr <= l || r <= ql || t[p].mx <= x)
      return;
    if (ql <= l && r <= qr && t[p].smx < x) {
      upper_node(p, x);
      return;
    }
    push(p);
    int m = (l + r) / 2;
    upper(ql, qr, x, p * 2, l, m);
    upper(ql, qr, x, p * 2 + 1, m, r);
    pull(p);
  }
  void lower(int ql, int qr, ll x, int p = 1, int l = 0, int r = -1) {
    if (r < 0)
      r = n;
    if (qr <= l || r <= ql || t[p].mn >= x)
      return;
    if (ql <= l && r <= qr && t[p].smn > x) {
      lower_node(p, x);
      return;
    }
    push(p);
    int m = (l + r) / 2;
    lower(ql, qr, x, p * 2, l, m);
    lower(ql, qr, x, p * 2 + 1, m, r);
    pull(p);
  }
  ll query(int ql, int qr, int p = 1, int l = 0, int r = -1) {
    if (r < 0)
      r = n;
    if (qr <= l || r <= ql)
      return 0;
    if (ql <= l && r <= qr)
      return t[p].sum;
    push(p);
    int m = (l + r) / 2;
    return query(ql, qr, p * 2, l, m) + query(ql, qr, p * 2 + 1, m, r);
  }
};
struct ModTree {
  int n;
  vector<ll> s, mx;
  ModTree(vector<ll> a) : n(a.size()), s(4 * n), mx(4 * n) {
    build(1, 0, n, a);
  }
  void build(int p, int l, int r, vector<ll> &a) {
    if (r - l == 1) {
      s[p] = mx[p] = a[l];
      return;
    }
    int m = (l + r) / 2;
    build(p * 2, l, m, a);
    build(p * 2 + 1, m, r, a);
    pull(p);
  }
  void pull(int p) {
    s[p] = s[p * 2] + s[p * 2 + 1];
    mx[p] = max(mx[p * 2], mx[p * 2 + 1]);
  }
  void mod(int ql, int qr, ll x, int p = 1, int l = 0, int r = -1) {
    if (r < 0)
      r = n;
    if (qr <= l || r <= ql || mx[p] < x)
      return;
    if (r - l == 1) {
      s[p] %= x;
      mx[p] = s[p];
      return;
    }
    int m = (l + r) / 2;
    mod(ql, qr, x, p * 2, l, m);
    mod(ql, qr, x, p * 2 + 1, m, r);
    pull(p);
  }
  void setv(int i, ll x, int p = 1, int l = 0, int r = -1) {
    if (r < 0)
      r = n;
    if (r - l == 1) {
      s[p] = mx[p] = x;
      return;
    }
    int m = (l + r) / 2;
    i < m ? setv(i, x, p * 2, l, m) : setv(i, x, p * 2 + 1, m, r);
    pull(p);
  }
  ll query(int ql, int qr, int p = 1, int l = 0, int r = -1) {
    if (r < 0)
      r = n;
    if (qr <= l || r <= ql)
      return 0;
    if (ql <= l && r <= qr)
      return s[p];
    int m = (l + r) / 2;
    return query(ql, qr, p * 2, l, m) + query(ql, qr, p * 2 + 1, m, r);
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
  Beats t(a);
  while (q--) {
    string op;
    int l, r;
    cin >> op >> l >> r;
    if (op == "UPPER") {
      ll x;
      cin >> x;
      t.upper(l - 1, r, x);
    } else if (op == "LOWER") {
      ll x;
      cin >> x;
      t.lower(l - 1, r, x);
    } else
      cout << t.query(l - 1, r) << '\n';
  }
}