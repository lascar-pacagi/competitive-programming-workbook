#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  if (!(cin >> n >> q))
    return 0;
  vector<int> a(n), p(n, -1), dep(n), sz(n, 1), heavy(n, -1), head(n), pos(n),
      ord = {0};
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
  for (int i = 0; i < (int)ord.size(); i++) {
    int u = ord[i];
    for (int v : g[u])
      if (v != p[u])
        p[v] = u, dep[v] = dep[u] + 1, ord.push_back(v);
  }
  for (int z = n - 1; z; z--) {
    int u = ord[z];
    sz[p[u]] += sz[u];
    if (heavy[p[u]] < 0 || sz[u] > sz[heavy[p[u]]])
      heavy[p[u]] = u;
  }
  int timer = 0;
  vector<pair<int, int>> todo = {{0, 0}};
  while (!todo.empty()) {
    auto [u, h] = todo.back();
    todo.pop_back();
    for (int x = u; x != -1; x = heavy[x]) {
      head[x] = h;
      pos[x] = timer++;
      for (int v : g[x])
        if (v != p[x] && v != heavy[x])
          todo.push_back({v, v});
    }
  }
  int z = 1;
  while (z < n)
    z *= 2;
  vector<int> t(2 * z, INT_MIN);
  for (int u = 0; u < n; u++)
    t[z + pos[u]] = a[u];
  for (int i = z - 1; i; i--)
    t[i] = max(t[2 * i], t[2 * i + 1]);
  auto query = [&](int l, int r) {
    int ans = INT_MIN;
    for (l += z, r += z + 1; l < r; l /= 2, r /= 2) {
      if (l & 1)
        ans = max(ans, t[l++]);
      if (r & 1)
        ans = max(ans, t[--r]);
    }
    return ans;
  };
  while (q--) {
    char c;
    int u, v;
    cin >> c >> u >> v;
    --u;
    if (c == 'U') {
      int x = z + pos[u];
      t[x] = v;
      for (x /= 2; x; x /= 2)
        t[x] = max(t[2 * x], t[2 * x + 1]);
    } else {
      --v;
      int ans = INT_MIN;
      while (head[u] != head[v]) {
        if (dep[head[u]] < dep[head[v]])
          swap(u, v);
        ans = max(ans, query(pos[head[u]], pos[u]));
        u = p[head[u]];
      }
      if (dep[u] > dep[v])
        swap(u, v);
      cout << max(ans, query(pos[u], pos[v])) << '\n';
    }
  }
}
