#include <bits/stdc++.h>
using namespace std;
struct N {
  int l = 0, r = 0, s = 0;
};
vector<N> t(1);
int add(int old, int l, int r, int p) {
  int x = t.size();
  t.push_back(t[old]);
  t[x].s++;
  if (r - l > 1) {
    int m = (l + r) / 2;
    if (p < m)
      t[x].l = add(t[old].l, l, m, p);
    else
      t[x].r = add(t[old].r, m, r, p);
  }
  return x;
}
int kth(int a, int b, int l, int r, int k) {
  if (r - l == 1)
    return l;
  int c = t[t[b].l].s - t[t[a].l].s, m = (l + r) / 2;
  return k <= c ? kth(t[a].l, t[b].l, l, m, k)
                : kth(t[a].r, t[b].r, m, r, k - c);
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  if (!(cin >> n >> q))
    return 0;
  vector<int> a(n), vals;
  for (int &x : a)
    cin >> x;
  vals = a;
  sort(vals.begin(), vals.end());
  vals.erase(unique(vals.begin(), vals.end()), vals.end());
  vector<vector<int>> g(n);
  for (int i = 1, u, v; i < n; i++) {
    cin >> u >> v;
    --u;
    --v;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  vector<int> p(n, -1), order, st = {0};
  while (!st.empty()) {
    int u = st.back();
    st.pop_back();
    order.push_back(u);
    for (int v : g[u])
      if (v != p[u])
        p[v] = u, st.push_back(v);
  }
  vector<int> tin(n), sz(n, 1);
  for (int i = 0; i < n; i++)
    tin[order[i]] = i;
  for (int i = n - 1; i; i--)
    sz[p[order[i]]] += sz[order[i]];
  vector<int> root(n + 1);
  for (int i = 0; i < n; i++) {
    int u = order[i],
        x = lower_bound(vals.begin(), vals.end(), a[u]) - vals.begin();
    root[i + 1] = add(root[i], 0, vals.size(), x);
  }
  while (q--) {
    int u, k;
    cin >> u >> k;
    --u;
    cout << vals[kth(root[tin[u]], root[tin[u] + sz[u]], 0, vals.size(), k)]
         << '\n';
  }
}
