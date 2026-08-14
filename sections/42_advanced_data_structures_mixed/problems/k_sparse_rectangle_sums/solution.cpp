#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct Op {
  char c;
  ll a, b, c1, d;
};
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int q;
  if (!(cin >> q))
    return 0;
  vector<Op> ops;
  vector<ll> xs;
  for (int i = 0; i < q; i++) {
    char c;
    cin >> c;
    if (c == 'U') {
      ll x, y, d;
      cin >> x >> y >> d;
      ops.push_back({c, x, y, d, 0});
      xs.push_back(x);
    } else {
      ll x1, y1, x2, y2;
      cin >> x1 >> y1 >> x2 >> y2;
      ops.push_back({c, x1, y1, x2, y2});
    }
  }
  sort(xs.begin(), xs.end());
  xs.erase(unique(xs.begin(), xs.end()), xs.end());
  int n = xs.size();
  vector<vector<ll>> ys(n + 1), bit(n + 1);
  for (auto &o : ops)
    if (o.c == 'U') {
      int x = lower_bound(xs.begin(), xs.end(), o.a) - xs.begin() + 1;
      for (int i = x; i <= n; i += i & -i)
        ys[i].push_back(o.b);
    }
  for (int i = 1; i <= n; i++) {
    sort(ys[i].begin(), ys[i].end());
    ys[i].erase(unique(ys[i].begin(), ys[i].end()), ys[i].end());
    bit[i].assign(ys[i].size() + 1, 0);
  }
  auto upd = [&](ll x, ll y, ll d) {
    for (int i = lower_bound(xs.begin(), xs.end(), x) - xs.begin() + 1; i <= n;
         i += i & -i)
      for (int j =
               lower_bound(ys[i].begin(), ys[i].end(), y) - ys[i].begin() + 1;
           j < (int)bit[i].size(); j += j & -j)
        bit[i][j] += d;
  };
  auto pref = [&](ll x, ll y) {
    ll ans = 0;
    for (int i = upper_bound(xs.begin(), xs.end(), x) - xs.begin(); i;
         i -= i & -i)
      for (int j = upper_bound(ys[i].begin(), ys[i].end(), y) - ys[i].begin();
           j; j -= j & -j)
        ans += bit[i][j];
    return ans;
  };
  for (auto &o : ops)
    if (o.c == 'U')
      upd(o.a, o.b, o.c1);
    else
      cout << pref(o.c1, o.d) - pref(o.a - 1, o.d) - pref(o.c1, o.b - 1) +
                  pref(o.a - 1, o.b - 1)
           << '\n';
}
