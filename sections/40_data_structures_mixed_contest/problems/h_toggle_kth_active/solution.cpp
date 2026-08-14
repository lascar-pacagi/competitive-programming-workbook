#include <bits/stdc++.h>
using namespace std;
struct BIT {
  int n;
  vector<int> t;
  BIT(int n) : n(n), t(n + 1) {}
  void add(int i, int v) {
    for (; i <= n; i += i & -i)
      t[i] += v;
  }
  int sum(int i) {
    int s = 0;
    for (; i; i -= i & -i)
      s += t[i];
    return s;
  }
  int kth(int k) {
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
  int n, q;
  if (!(cin >> n >> q))
    return 0;
  BIT b(n);
  vector<char> on(n + 1);
  while (q--) {
    char c;
    int x;
    cin >> c >> x;
    if (c == 'T') {
      b.add(x, on[x] ? -1 : 1);
      on[x] ^= 1;
    } else
      cout << (b.sum(n) < x ? -1 : b.kth(x)) << '\n';
  }
}
