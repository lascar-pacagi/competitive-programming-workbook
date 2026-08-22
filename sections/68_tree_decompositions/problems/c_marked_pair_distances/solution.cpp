#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  if (!(cin >> n >> q)) return 0;
  vector<vector<pair<int, int>>> g(n);
  for (int i = 1, u, v, w; i < n; i++) {
    cin >> u >> v >> w;
    --u;
    --v;
    g[u].push_back({v, w});
    g[v].push_back({u, w});
  }
  int log = 1;
  while ((1 << log) <= n) log++;
  vector<vector<int>> up(log, vector<int>(n));
  vector<int> tin(n), tout(n), depth(n);
  vector<int64> distance(n);
  int timer = 0;
  vector<tuple<int, int, int, int>> stack{{0, 0, 0, 0}};
  while (!stack.empty()) {
    auto [u, p, w, state] = stack.back();
    stack.pop_back();
    if (!state) {
      tin[u] = timer++;
      up[0][u] = p;
      for (int j = 1; j < log; j++) up[j][u] = up[j - 1][up[j - 1][u]];
      stack.push_back({u, p, w, 1});
      for (auto it = g[u].rbegin(); it != g[u].rend(); ++it)
        if (it->first != p) {
          depth[it->first] = depth[u] + 1;
          distance[it->first] = distance[u] + it->second;
          stack.push_back({it->first, u, it->second, 0});
        }
    } else
      tout[u] = timer - 1;
  }
  auto ancestor = [&](int u, int v) { return tin[u] <= tin[v] && tout[v] <= tout[u]; };
  auto lca = [&](int u, int v) {
    if (ancestor(u, v)) return u;
    if (ancestor(v, u)) return v;
    for (int j = log - 1; j >= 0; j--)
      if (!ancestor(up[j][u], v)) u = up[j][u];
    return up[0][u];
  };
  vector<char> marked(n);
  vector<int> count(n), virtual_parent(n);
  while (q--) {
    int k;
    cin >> k;
    vector<int> nodes(k);
    for (int& u : nodes) {
      cin >> u;
      --u;
      marked[u] = 1;
    }
    sort(nodes.begin(), nodes.end(), [&](int a, int b) { return tin[a] < tin[b]; });
    int original = nodes.size();
    for (int i = 1; i < original; i++) nodes.push_back(lca(nodes[i - 1], nodes[i]));
    sort(nodes.begin(), nodes.end(), [&](int a, int b) { return tin[a] < tin[b]; });
    nodes.erase(unique(nodes.begin(), nodes.end()), nodes.end());
    vector<int> st;
    for (int u : nodes) {
      while (!st.empty() && !ancestor(st.back(), u)) st.pop_back();
      virtual_parent[u] = st.empty() ? -1 : st.back();
      st.push_back(u);
      count[u] = marked[u];
    }
    int64 answer = 0;
    for (int i = nodes.size() - 1; i >= 0; i--) {
      int u = nodes[i];
      int p = virtual_parent[u];
      if (p != -1) {
        answer += (distance[u] - distance[p]) * count[u] * (k - count[u]);
        count[p] += count[u];
      }
    }
    cout << answer << '\n';
    for (int u : nodes) marked[u] = 0;
  }
}
