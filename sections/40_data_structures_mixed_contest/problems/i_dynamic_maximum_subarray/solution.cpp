#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct N {
  ll sum, pref, suff, best;
};
N one(ll x) { return {x, x, x, x}; }
N join(N a, N b) {
  return {
      a.sum + b.sum,
      max(a.pref, a.sum + b.pref),
      max(b.suff, b.sum + a.suff),
      max({a.best, b.best, a.suff + b.pref})
  };
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  if (!(cin >> n >> q))
    return 0;
  int z = 1;
  while (z < n)
    z *= 2;
  const ll X = -(1LL << 60);
  vector<N> t(2 * z, {0, X, X, X});
  for (int i = 0; i < n; i++) {
    ll x;
    cin >> x;
    t[z + i] = one(x);
  }
  for (int i = z - 1; i; i--)
    t[i] = join(t[2 * i], t[2 * i + 1]);
  while (q--) {
    int p;
    ll x;
    cin >> p >> x;
    p = z + p - 1;
    t[p] = one(x);
    for (p /= 2; p; p /= 2)
      t[p] = join(t[2 * p], t[2 * p + 1]);
    cout << t[1].best << '\n';
  }
}
