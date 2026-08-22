#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  if (!(cin >> n)) return 0;
  vector<int> color(n);
  for (int& x : color) cin >> x;
  vector<vector<int>> g(n);
  for (int i = 1, u, v; i < n; i++) {
    cin >> u >> v;
    --u;
    --v;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  vector<int> parent(n, -1), order{0};
  for (int i = 0; i < (int)order.size(); i++) {
    int u = order[i];
    for (int v : g[u])
      if (v != parent[u]) parent[v] = u, order.push_back(v);
  }
  vector<unordered_map<int, int>*> maps(n);
  vector<int> best(n), ways(n);
  for (int at = n - 1; at >= 0; at--) {
    int u = order[at], base = -1;
    for (int v : g[u])
      if (parent[v] == u && (base < 0 || maps[v]->size() > maps[base]->size()))
        base = v;
    if (base < 0)
      maps[u] = new unordered_map<int, int>();
    else
      maps[u] = maps[base], best[u] = best[base], ways[u] = ways[base];
    auto add = [&](int c, int amount) {
      int value = ((*maps[u])[c] += amount);
      if (value > best[u])
        best[u] = value, ways[u] = 1;
      else if (value == best[u])
        ways[u]++;
    };
    for (int v : g[u])
      if (parent[v] == u && v != base) {
        for (auto [c, x] : *maps[v]) add(c, x);
        delete maps[v];
      }
    add(color[u], 1);
  }
  for (int u = 0; u < n; u++) cout << best[u] << ' ' << ways[u] << '\n';
  delete maps[0];
}
