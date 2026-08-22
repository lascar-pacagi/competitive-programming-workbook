#include <bits/stdc++.h>
using namespace std;
struct KRT {
  int n, z, L;
  vector<int> dsu, parent, dep, weight, sz, component;
  vector<vector<int>> up, child;
  int find(int x) { return dsu[x] == x ? x : dsu[x] = find(dsu[x]); }
  KRT(int n, vector<array<int, 3>> e)
      : n(n), z(n), dsu(2 * n + 5), parent(2 * n + 5), dep(2 * n + 5),
        weight(2 * n + 5, -1), sz(2 * n + 5, 1), child(2 * n + 5) {
    iota(dsu.begin(), dsu.end(), 0);
    iota(parent.begin(), parent.end(), 0);
    sort(e.begin(), e.end());
    for (auto [w, u, v] : e) {
      u = find(u);
      v = find(v);
      if (u == v)
        continue;
      int x = z++;
      weight[x] = w;
      sz[x] = sz[u] + sz[v];
      child[x] = {u, v};
      parent[u] = parent[v] = x;
      dsu[u] = dsu[v] = dsu[x] = x;
    }
    vector<int> roots;
    for (int i = 0; i < z; i++)
      if (parent[i] == i)
        roots.push_back(i);
    for (int r : roots) {
      vector<int> st = {r};
      while (!st.empty()) {
        int x = st.back();
        st.pop_back();
        for (int y : child[x])
          dep[y] = dep[x] + 1, st.push_back(y);
      }
    }
    L = max(1, (int)bit_width((unsigned)z));
    up.assign(L, vector<int>(z));
    for (int i = 0; i < z; i++)
      up[0][i] = parent[i];
    for (int j = 1; j < L; j++)
      for (int i = 0; i < z; i++)
        up[j][i] = up[j - 1][up[j - 1][i]];
    component.resize(n);
    for (int i = 0; i < n; i++)
      component[i] = find(i);
  }
  int climb(int v, int x) {
    for (int j = L - 1; j >= 0; j--) {
      int q = up[j][v];
      if (q != v && weight[q] <= x)
        v = q;
    }
    return v;
  }
  int lca(int a, int b) {
    if (component[a] != component[b])
      return -1;
    if (dep[a] < dep[b])
      swap(a, b);
    int d = dep[a] - dep[b];
    for (int j = 0; j < L; j++)
      if (d >> j & 1)
        a = up[j][a];
    if (a == b)
      return a;
    for (int j = L - 1; j >= 0; j--)
      if (up[j][a] != up[j][b])
        a = up[j][a], b = up[j][b];
    return up[0][a];
  }
};
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m, q;
  cin >> n >> m >> q;
  vector<array<int, 3>> e(m);
  for (int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    e[i] = {i + 1, u - 1, v - 1};
  }
  KRT t(n, e);
  while (q--) {
    int u, v;
    cin >> u >> v;
    --u;
    --v;
    if (u == v)
      cout << 0 << '\n';
    else {
      int x = t.lca(u, v);
      cout << (x < 0 ? -1 : t.weight[x]) << '\n';
    }
  }
}