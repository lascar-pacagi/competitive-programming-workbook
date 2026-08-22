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
  int log = bit_width((unsigned)n);
  vector<vector<int>> up(log, vector<int>(n));
  vector<int> tin(n), tout(n);
  vector<int64> distance(n);
  int timer = 0;
  vector<tuple<int, int, int>> stack{{0, 0, 0}};
  while (!stack.empty()) {
    auto [u, p, state] = stack.back();
    stack.pop_back();
    if (!state) {
      tin[u] = timer++;
      up[0][u] = p;
      for (int j = 1; j < log; j++) up[j][u] = up[j - 1][up[j - 1][u]];
      stack.push_back({u, p, 1});
      for (auto it = g[u].rbegin(); it != g[u].rend(); ++it)
        if (it->first != p)
          distance[it->first] = distance[u] + it->second,
          stack.push_back({it->first, u, 0});
    } else
      tout[u] = timer - 1;
  }
  auto ancestor = [&](int u, int v) { return tin[u] <= tin[v] && tin[v] <= tout[u]; };
  auto lca = [&](int u, int v) {
    if (ancestor(u, v)) return u;
    if (ancestor(v, u)) return v;
    for (int j = log - 1; j >= 0; j--)
      if (!ancestor(up[j][u], v)) u = up[j][u];
    return up[0][u];
  };
  vector<int64> weight(n), subtree(n);
  vector<int> parent(n);
  while (q--) {
    int k;
    cin >> k;
    vector<int> nodes(k);
    int64 total = 0;
    for (int i = 0; i < k; i++) {
      cin >> nodes[i] >> weight[--nodes[i]];
      total += weight[nodes[i]];
    }
    sort(nodes.begin(), nodes.end(), [&](int a, int b) { return tin[a] < tin[b]; });
    for (int i = 1; i < k; i++) nodes.push_back(lca(nodes[i - 1], nodes[i]));
    sort(nodes.begin(), nodes.end(), [&](int a, int b) { return tin[a] < tin[b]; });
    nodes.erase(unique(nodes.begin(), nodes.end()), nodes.end());
    vector<int> st;
    for (int u : nodes) {
      while (!st.empty() && !ancestor(st.back(), u)) st.pop_back();
      parent[u] = st.empty() ? -1 : st.back();
      st.push_back(u);
      subtree[u] = weight[u];
    }
    int64 answer = 0;
    for (int i = nodes.size() - 1; i >= 0; i--) {
      int u = nodes[i], p = parent[u];
      if (p != -1) {
        answer += (distance[u] - distance[p]) * subtree[u] * (total - subtree[u]);
        subtree[p] += subtree[u];
      }
    }
    cout << answer << '\n';
    for (int u : nodes) weight[u] = 0;
  }
}
