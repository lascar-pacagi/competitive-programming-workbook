#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct Wavelet {
  int B, n;
  vector<ll> vals;
  vector<vector<int>> z;
  vector<vector<ll>> zs;
  vector<int> mid;
  Wavelet(vector<ll> a) : n(a.size()) {
    vals = a;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    B = max(1, (int)bit_width((unsigned)max(1, (int)vals.size() - 1)));
    vector<int> r(n);
    for (int i = 0; i < n; i++)
      r[i] = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin();
    for (int b = B - 1; b >= 0; b--) {
      z.push_back(vector<int>(n + 1));
      zs.push_back(vector<ll>(n + 1));
      vector<int> r0, r1;
      vector<ll> a0, a1;
      for (int i = 0; i < n; i++) {
        bool zero = !(r[i] >> b & 1);
        z.back()[i + 1] = z.back()[i] + zero;
        zs.back()[i + 1] = zs.back()[i] + (zero ? a[i] : 0);
        (zero ? r0 : r1).push_back(r[i]);
        (zero ? a0 : a1).push_back(a[i]);
      }
      mid.push_back(r0.size());
      r0.insert(r0.end(), r1.begin(), r1.end());
      a0.insert(a0.end(), a1.begin(), a1.end());
      r.swap(r0);
      a.swap(a0);
    }
  }
  ll kth(int l, int r, int k) {
    int rank = 0;
    for (int d = 0; d < B; d++) {
      int q = z[d][r] - z[d][l], b = B - 1 - d;
      if (k <= q)
        l = z[d][l], r = z[d][r];
      else
        k -= q, rank |= 1 << b, l = mid[d] + l - z[d][l],
                                r = mid[d] + r - z[d][r];
    }
    return vals[rank];
  }
  int lte(int l, int r, ll x) {
    int lim = upper_bound(vals.begin(), vals.end(), x) - vals.begin();
    if (lim == (int)vals.size())
      return r - l;
    int ans = 0;
    for (int d = 0; d < B; d++) {
      int b = B - 1 - d;
      if (lim >> b & 1)
        ans += z[d][r] - z[d][l], l = mid[d] + l - z[d][l],
                                  r = mid[d] + r - z[d][r];
      else
        l = z[d][l], r = z[d][r];
    }
    return ans;
  }
  ll sumk(int l, int r, int k) {
    ll ans = 0;
    int rank = 0;
    for (int d = 0; d < B; d++) {
      int q = z[d][r] - z[d][l], b = B - 1 - d;
      if (k <= q)
        l = z[d][l], r = z[d][r];
      else
        ans += zs[d][r] - zs[d][l], k -= q, rank |= 1 << b,
            l = mid[d] + l - z[d][l], r = mid[d] + r - z[d][r];
    }
    return ans + vals[rank] * k;
  }
};
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  cin >> n >> q;
  vector<ll> a(n);
  for (auto &x : a)
    cin >> x;
  Wavelet w(a);
  while (q--) {
    int l, r;
    ll x;
    cin >> l >> r >> x;
    cout << w.lte(l - 1, r, x) << '\n';
  }
}