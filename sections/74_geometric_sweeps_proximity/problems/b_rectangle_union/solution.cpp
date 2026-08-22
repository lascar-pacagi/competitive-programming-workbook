#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct E {
  ll x, y1, y2;
  int d;
};
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  if (!(cin >> n))
    return 0;
  vector<E> e;
  vector<ll> ys;
  for (int i = 0; i < n; ++i) {
    ll x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    if (x1 > x2)
      swap(x1, x2);
    if (y1 > y2)
      swap(y1, y2);
    if (x1 == x2 || y1 == y2)
      continue;
    e.push_back({x1, y1, y2, 1});
    e.push_back({x2, y1, y2, -1});
    ys.push_back(y1);
    ys.push_back(y2);
  }
  if (e.empty()) {
    cout << 0 << '\n';
    return 0;
  }
  sort(ys.begin(), ys.end());
  ys.erase(unique(ys.begin(), ys.end()), ys.end());
  sort(e.begin(), e.end(), [](E a, E b) { return a.x < b.x; });
  int m = ys.size() - 1;
  vector<int> cover(4 * m);
  vector<ll> len(4 * m);
  function<void(int, int, int, int, int, int)> upd =
      [&](int x, int l, int r, int ql, int qr, int d) {
        if (qr <= l || r <= ql)
          return;
        if (ql <= l && r <= qr)
          cover[x] += d;
        else {
          int mid = (l + r) / 2;
          upd(2 * x, l, mid, ql, qr, d);
          upd(2 * x + 1, mid, r, ql, qr, d);
        }
        if (cover[x])
          len[x] = ys[r] - ys[l];
        else
          len[x] = r - l == 1 ? 0 : len[2 * x] + len[2 * x + 1];
      };
  ll ans = 0, last = e[0].x;
  for (int i = 0; i < (int)e.size();) {
    ll x = e[i].x;
    ans += (x - last) * len[1];
    while (i < (int)e.size() && e[i].x == x) {
      int l = lower_bound(ys.begin(), ys.end(), e[i].y1) - ys.begin(),
          r = lower_bound(ys.begin(), ys.end(), e[i].y2) - ys.begin();
      upd(1, 0, m, l, r, e[i].d);
      ++i;
    }
    last = x;
  }
  cout << ans << '\n';
}
