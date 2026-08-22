#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
using i128 = __int128_t;
string show(i128 x) {
  if (x == 0)
    return "0";
  bool neg = x < 0;
  if (neg)
    x = -x;
  string s;
  while (x)
    s.push_back('0' + x % 10), x /= 10;
  if (neg)
    s.push_back('-');
  reverse(s.begin(), s.end());
  return s;
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  int64 k;
  if (!(cin >> n >> k))
    return 0;
  vector<int64> a(n), b(n), cap(n);
  int64 total = 0;
  for (int i = 0; i < n; ++i)
    cin >> a[i] >> b[i] >> cap[i], total += cap[i];
  if (total < k) {
    cout << "IMPOSSIBLE\n";
    return 0;
  }
  auto count = [&](i128 threshold) {
    int64 result = 0;
    for (int i = 0; i < n; ++i) {
      if (threshold < a[i] + b[i])
        continue;
      int64 x = min<i128>(cap[i], (threshold - b[i] + a[i]) / (2 * a[i]));
      result += min(cap[i], x);
      if (result >= k)
        return k;
    }
    return result;
  };
  if (k == 0) {
    cout << "0\n";
    return 0;
  }
  i128 lo = 0, hi = 0;
  bool first = true;
  for (int i = 0; i < n; ++i)
    if (cap[i]) {
      i128 first_cost = (i128)a[i] + b[i];
      i128 last_cost = (i128)a[i] * (2 * (i128)cap[i] - 1) + b[i];
      if (first)
        lo = first_cost, hi = last_cost, first = false;
      else
        lo = min(lo, first_cost), hi = max(hi, last_cost);
    }
  while (lo < hi) {
    i128 mid = lo + (hi - lo) / 2;
    if (count(mid) >= k)
      hi = mid;
    else
      lo = mid + 1;
  }
  i128 threshold = lo, answer = 0;
  int64 used = 0;
  for (int i = 0; i < n; ++i) {
    int64 x = 0;
    if (threshold - 1 >= a[i] + b[i])
      x = min<i128>(cap[i], (threshold - 1 - b[i] + a[i]) / (2 * a[i]));
    used += x;
    answer += (i128)a[i] * x * x + (i128)b[i] * x;
  }
  answer += (i128)(k - used) * threshold;
  cout << show(answer) << '\n';
}
