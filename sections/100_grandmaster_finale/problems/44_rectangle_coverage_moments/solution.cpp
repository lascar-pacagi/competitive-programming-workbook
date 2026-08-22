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
  vector<ll> one(4 * m), two(4 * m);
  function<void(int, int, int)> pull = [&](int x, int l, int r) {
    ll full = ys[r] - ys[l],
       child1 = r - l == 1 ? 0 : one[2 * x] + one[2 * x + 1],
       child2 = r - l == 1 ? 0 : two[2 * x] + two[2 * x + 1];
    if (cover[x] >= 2)
      one[x] = two[x] = full;
    else if (cover[x] == 1)
      one[x] = full, two[x] = child1;
    else
      one[x] = child1, two[x] = child2;
  };
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
        pull(x, l, r);
      };
  ll ans = 0, last = e[0].x;
  for (int i = 0; i < (int)e.size();) {
    ll x = e[i].x;
    ans += (x - last) * two[1];
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
