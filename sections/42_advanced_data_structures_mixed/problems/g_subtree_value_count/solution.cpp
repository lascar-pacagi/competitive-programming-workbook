#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  if (!(cin >> n >> q))
    return 0;
  vector<int> a(n);
  for (int &x : a)
    cin >> x;
  vector<vector<int>> g(n);
  for (int i = 1, u, v; i < n; i++) {
    cin >> u >> v;
    --u;
    --v;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  vector<int> tin(n), tout(n), par(n, -1), order, st = {0};
  while (!st.empty()) {
    int u = st.back();
    st.pop_back();
    order.push_back(u);
    for (int v : g[u])
      if (v != par[u])
        par[v] = u, st.push_back(v);
  }
  for (int i = 0; i < n; i++)
    tin[order[i]] = i;
  vector<int> sz(n, 1);
  for (int i = n - 1; i; i--)
    sz[par[order[i]]] += sz[order[i]];
  for (int u = 0; u < n; u++)
    tout[u] = tin[u] + sz[u];
  int z = 1;
  while (z < n)
    z *= 2;
  vector<vector<int>> t(2 * z);
  for (int u = 0; u < n; u++)
    t[z + tin[u]] = {a[u]};
  for (int i = z - 1; i; i--) {
    auto &x = t[2 * i];
    auto &y = t[2 * i + 1];
    t[i].resize(x.size() + y.size());
    merge(x.begin(), x.end(), y.begin(), y.end(), t[i].begin());
  }
  while (q--) {
    int u, lo, hi;
    cin >> u >> lo >> hi;
    --u;
    int l = z + tin[u], r = z + tout[u], ans = 0;
    while (l < r) {
      if (l & 1) {
        auto &v = t[l++];
        ans += upper_bound(v.begin(), v.end(), hi) -
               lower_bound(v.begin(), v.end(), lo);
      }
      if (r & 1) {
        auto &v = t[--r];
        ans += upper_bound(v.begin(), v.end(), hi) -
               lower_bound(v.begin(), v.end(), lo);
      }
      l /= 2;
      r /= 2;
    }
    cout << ans << '\n';
  }
}
