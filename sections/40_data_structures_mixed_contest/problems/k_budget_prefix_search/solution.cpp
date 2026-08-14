#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct Node {
  ll sum, pref;
};
struct Seg {
  int n;
  vector<Node> t;
  Seg(vector<ll> &a) : n(a.size()), t(4 * n) { build(1, 0, n, a); }
  void pull(int x) {
    t[x] = {t[2 * x].sum + t[2 * x + 1].sum,
            max(t[2 * x].pref, t[2 * x].sum + t[2 * x + 1].pref)};
  }
  void build(int x, int l, int r, vector<ll> &a) {
    if (r - l == 1) {
      t[x] = {a[l], a[l]};
      return;
    }
    int m = (l + r) / 2;
    build(2 * x, l, m, a);
    build(2 * x + 1, m, r, a);
    pull(x);
  }
  void set_value(int x, int l, int r, int p, ll v) {
    if (r - l == 1) {
      t[x] = {v, v};
      return;
    }
    int m = (l + r) / 2;
    if (p < m)
      set_value(2 * x, l, m, p, v);
    else
      set_value(2 * x + 1, m, r, p, v);
    pull(x);
  }
  int first(int x, int l, int r, int ql, ll budget, ll &sum) {
    if (r <= ql)
      return -1;
    if (ql <= l && sum + t[x].pref <= budget) {
      sum += t[x].sum;
      return -1;
    }
    if (r - l == 1)
      return l;
    int m = (l + r) / 2, res = first(2 * x, l, m, ql, budget, sum);
    return res < 0 ? first(2 * x + 1, m, r, ql, budget, sum) : res;
  }
};
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  if (!(cin >> n >> q))
    return 0;
  vector<ll> a(n);
  for (ll &x : a)
    cin >> x;
  Seg s(a);
  while (q--) {
    char c;
    int i;
    ll x;
    cin >> c >> i >> x;
    --i;
    if (c == 'U')
      s.set_value(1, 0, n, i, x);
    else {
      ll sum = 0;
      int answer = s.first(1, 0, n, i, x, sum);
      cout << (answer < 0 ? -1 : answer + 1) << '\n';
    }
  }
}
