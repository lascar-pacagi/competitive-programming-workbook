#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF = LLONG_MAX;
struct P {
  ll x, y;
};
ll d2(P a, P b) {
  ll x = a.x - b.x, y = a.y - b.y;
  return x * x + y * y;
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  if (!(cin >> n))
    return 0;
  vector<P> a(n), tmp(n);
  for (auto &p : a)
    cin >> p.x >> p.y;
  sort(a.begin(), a.end(),
       [](P p, P q) { return tie(p.x, p.y) < tie(q.x, q.y); });
  function<ll(int, int)> solve = [&](int l, int r) {
    if (r - l <= 3) {
      ll d = INF;
      for (int i = l; i < r; ++i)
        for (int j = i + 1; j < r; ++j)
          d = min(d, d2(a[i], a[j]));
      sort(a.begin() + l, a.begin() + r, [](P p, P q) { return p.y < q.y; });
      return d;
    }
    int m = (l + r) / 2;
    ll mid = a[m].x, d = min(solve(l, m), solve(m, r));
    merge(a.begin() + l, a.begin() + m, a.begin() + m, a.begin() + r,
          tmp.begin(), [](P p, P q) { return p.y < q.y; });
    copy(tmp.begin(), tmp.begin() + r - l, a.begin() + l);
    vector<P> s;
    for (int i = l; i < r; ++i)
      if ((a[i].x - mid) * (a[i].x - mid) < d) {
        for (int j = (int)s.size() - 1;
             j >= 0 && (a[i].y - s[j].y) * (a[i].y - s[j].y) < d; --j)
          d = min(d, d2(a[i], s[j]));
        s.push_back(a[i]);
      }
    return d;
  };
  cout << solve(0, n) << '\n';
}
