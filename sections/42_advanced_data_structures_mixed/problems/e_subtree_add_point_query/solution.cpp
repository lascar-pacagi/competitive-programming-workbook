#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  if (!(cin >> n >> q))
    return 0;
  vector<ll> a(n);
  for (auto &x : a)
    cin >> x;
  vector<vector<int>> g(n);
  for (int i = 1, u, v; i < n; i++) {
    cin >> u >> v;
    --u;
    --v;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  vector<int> tin(n), tout(n), par(n, -1), it(n);
  int timer = 0;
  vector<int> st = {0};
  while (!st.empty()) {
    int u = st.back();
    if (!it[u])
      tin[u] = ++timer;
    if (it[u] < (int)g[u].size()) {
      int v = g[u][it[u]++];
      if (v == par[u])
        continue;
      par[v] = u;
      st.push_back(v);
    } else {
      tout[u] = timer;
      st.pop_back();
    }
  }
  vector<ll> bit(n + 2);
  auto add = [&](int i, ll x) {
    for (; i <= n + 1; i += i & -i)
      bit[i] += x;
  };
  auto get = [&](int i) {
    ll s = 0;
    for (; i; i -= i & -i)
      s += bit[i];
    return s;
  };
  while (q--) {
    char c;
    int u;
    cin >> c >> u;
    --u;
    if (c == 'A') {
      ll x;
      cin >> x;
      add(tin[u], x);
      add(tout[u] + 1, -x);
    } else
      cout << a[u] + get(tin[u]) << '\n';
  }
}
