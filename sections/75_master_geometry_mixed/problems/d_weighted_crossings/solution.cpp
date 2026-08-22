#include <bits/stdc++.h>
using namespace std;
struct BIT {
  vector<long long> t;
  BIT(int n) : t(n + 1) {}
  void add(int i, long long v) {
    for (++i; i < (int)t.size(); i += i & -i)
      t[i] += v;
  }
  long long sum(int i) {
    long long s = 0;
    for (; i; i -= i & -i)
      s += t[i];
    return s;
  }
  long long range(int l, int r) { return sum(r) - sum(l); }
};
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int h, v;
  if (!(cin >> h >> v))
    return 0;
  struct E {
    long long x;
    int type;
    long long y1, y2, w;
  };
  vector<E> e;
  vector<long long> ys;
  for (int i = 0; i < h; ++i) {
    long long x1, x2, y, w;
    cin >> x1 >> x2 >> y >> w;
    if (x1 > x2)
      swap(x1, x2);
    e.push_back({x1, 0, y, y, w});
    e.push_back({x2, 2, y, y, -w});
    ys.push_back(y);
  }
  for (int i = 0; i < v; ++i) {
    long long x, y1, y2, w;
    cin >> x >> y1 >> y2 >> w;
    if (y1 > y2)
      swap(y1, y2);
    e.push_back({x, 1, y1, y2, w});
    ys.push_back(y1);
    ys.push_back(y2);
  }
  sort(ys.begin(), ys.end());
  ys.erase(unique(ys.begin(), ys.end()), ys.end());
  sort(e.begin(), e.end(),
       [](E a, E b) { return tie(a.x, a.type) < tie(b.x, b.type); });
  BIT bit(ys.size());
  long long ans = 0;
  for (auto z : e) {
    if (z.type != 1)
      bit.add(lower_bound(ys.begin(), ys.end(), z.y1) - ys.begin(), z.w);
    else {
      int l = lower_bound(ys.begin(), ys.end(), z.y1) - ys.begin(),
          r = upper_bound(ys.begin(), ys.end(), z.y2) - ys.begin();
      ans += z.w * bit.range(l, r);
    }
  }
  cout << ans << '\n';
}
