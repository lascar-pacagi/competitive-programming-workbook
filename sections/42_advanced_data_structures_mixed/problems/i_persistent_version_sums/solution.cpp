#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct N {
  int l = 0, r = 0;
  ll s = 0;
};
vector<N> t(1);
int build(int l, int r, vector<ll> &a) {
  int x = t.size();
  t.push_back({});
  if (r - l == 1) {
    t[x].s = a[l];
    return x;
  }
  int m = (l + r) / 2;
  t[x].l = build(l, m, a);
  t[x].r = build(m, r, a);
  t[x].s = t[t[x].l].s + t[t[x].r].s;
  return x;
}
int update(int old, int l, int r, int p, ll v) {
  int x = t.size();
  t.push_back(t[old]);
  if (r - l == 1) {
    t[x].s = v;
    return x;
  }
  int m = (l + r) / 2;
  if (p < m)
    t[x].l = update(t[old].l, l, m, p, v);
  else
    t[x].r = update(t[old].r, m, r, p, v);
  t[x].s = t[t[x].l].s + t[t[x].r].s;
  return x;
}
ll query(int x, int l, int r, int ql, int qr) {
  if (ql >= r || qr <= l)
    return 0;
  if (ql <= l && r <= qr)
    return t[x].s;
  int m = (l + r) / 2;
  return query(t[x].l, l, m, ql, qr) + query(t[x].r, m, r, ql, qr);
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  if (!(cin >> n >> q))
    return 0;
  vector<ll> a(n);
  for (auto &x : a)
    cin >> x;
  vector<int> root = {build(0, n, a)};
  while (q--) {
    char c;
    int v, l;
    cin >> c >> v >> l;
    if (c == 'U') {
      ll x;
      cin >> x;
      root.push_back(update(root[v], 0, n, l - 1, x));
    } else {
      int r;
      cin >> r;
      cout << query(root[v], 0, n, l - 1, r) << '\n';
    }
  }
}
