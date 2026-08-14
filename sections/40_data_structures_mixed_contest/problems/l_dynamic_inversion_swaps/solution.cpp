#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  if (!(cin >> n >> q))
    return 0;
  vector<int> a(n);
  for (int &x : a)
    cin >> x;
  vector<int> bit(n + 1);
  auto add = [&](int i) {
    for (; i <= n; i += i & -i)
      bit[i]++;
  };
  auto sum = [&](int i) {
    int s = 0;
    for (; i; i -= i & -i)
      s += bit[i];
    return s;
  };
  ll inv = 0;
  for (int x : a) {
    inv += sum(n) - sum(x);
    add(x);
  }
  int B = 450, nb = (n + B - 1) / B;
  vector<vector<int>> blk(nb);
  auto rebuild = [&](int b) {
    blk[b].assign(a.begin() + b * B, a.begin() + min(n, (b + 1) * B));
    sort(blk[b].begin(), blk[b].end());
  };
  for (int b = 0; b < nb; b++)
    rebuild(b);
  auto count = [&](int l, int r, int lo, int hi) {
    int ans = 0;
    if (l > r || lo >= hi)
      return 0;
    while (l <= r && l % B) {
      ans += lo < a[l] && a[l] < hi;
      l++;
    }
    while (l + B - 1 <= r) {
      auto &v = blk[l / B];
      ans += lower_bound(v.begin(), v.end(), hi) -
             upper_bound(v.begin(), v.end(), lo);
      l += B;
    }
    while (l <= r) {
      ans += lo < a[l] && a[l] < hi;
      l++;
    }
    return ans;
  };
  while (q--) {
    int i, j;
    cin >> i >> j;
    --i;
    --j;
    if (i > j)
      swap(i, j);
    if (i != j) {
      int x = a[i], y = a[j], c = count(i + 1, j - 1, min(x, y), max(x, y));
      ll d = 1 + 2LL * c;
      inv += (x < y ? d : -d);
      swap(a[i], a[j]);
      rebuild(i / B);
      if (i / B != j / B)
        rebuild(j / B);
    }
    cout << inv << '\n';
  }
}
