#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct BIT {
  int n;
  vector<ll> t;
  BIT(int n) : n(n), t(n + 1) {}
  void add(int i, ll v) {
    for (; i <= n; i += i & -i)
      t[i] += v;
  }
  ll sum(int i) {
    ll s = 0;
    for (; i; i -= i & -i)
      s += t[i];
    return s;
  }
  int kth(ll k) {
    int p = 0;
    for (int d = bit_floor((unsigned)n); d; d >>= 1)
      if (p + d <= n && t[p + d] < k)
        k -= t[p += d];
    return p + 1;
  }
};
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, k;
  if (!(cin >> n >> k))
    return 0;
  vector<ll> a(n), v;
  for (ll &x : a)
    cin >> x;
  v = a;
  sort(v.begin(), v.end());
  v.erase(unique(v.begin(), v.end()), v.end());
  BIT cnt(v.size()), sum(v.size());
  auto add = [&](ll x, int d) {
    int p = lower_bound(v.begin(), v.end(), x) - v.begin() + 1;
    cnt.add(p, d);
    sum.add(p, d * x);
  };
  for (int i = 0; i < k; i++)
    add(a[i], 1);
  for (int l = 0;; l++) {
    int p = cnt.kth((k + 1) / 2);
    ll m = v[p - 1];
    ll cl = cnt.sum(p);
    ll sl = sum.sum(p);
    ll ct = cnt.sum(v.size());
    ll st = sum.sum(v.size());
    ll ans = m * cl - sl + (st - sl) - m * (ct - cl);
    if (l)
      cout << ' ';
    cout << ans;
    if (l + k == n)
      break;
    add(a[l], -1);
    add(a[l + k], 1);
  }
  cout << '\n';
}
