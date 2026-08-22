#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  if (!(cin >> n >> q)) return 0;
  vector<vector<int>> g(n);
  for (int i = 1, u, v; i < n; i++) {
    cin >> u >> v;
    --u;
    --v;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  vector<char> blocked(n), active(n);
  vector<int> parent(n, -1), subtree(n);
  vector<int> traversal_parent(n), seen(n);
  int stamp = 0;
  vector<vector<pair<int, int>>> path(n);
  function<void(int, int)> decompose = [&](int entry, int centroid_parent) {
    ++stamp;
    vector<int> nodes;
    nodes.push_back(entry);
    seen[entry] = stamp;
    traversal_parent[entry] = -1;
    for (int i = 0; i < (int)nodes.size(); i++) {
      int u = nodes[i];
      for (int v : g[u])
        if (!blocked[v] && seen[v] != stamp) {
          seen[v] = stamp;
          traversal_parent[v] = u;
          nodes.push_back(v);
        }
    }
    for (int i = nodes.size() - 1; i >= 0; i--) {
      int u = nodes[i];
      subtree[u] = 1;
      for (int v : g[u])
        if (!blocked[v] && seen[v] == stamp && traversal_parent[v] == u)
          subtree[u] += subtree[v];
    }
    int total = nodes.size(), centroid = entry;
    for (int u : nodes) {
      int largest = total - subtree[u];
      for (int v : g[u])
        if (!blocked[v] && seen[v] == stamp && traversal_parent[v] == u)
          largest = max(largest, subtree[v]);
      if (largest * 2 <= total) {
        centroid = u;
        break;
      }
    }
    parent[centroid] = centroid_parent;
    vector<tuple<int, int, int>> stack{{centroid, -1, 0}};
    while (!stack.empty()) {
      auto [u, p, d] = stack.back();
      stack.pop_back();
      path[u].push_back({centroid, d});
      for (int v : g[u])
        if (v != p && !blocked[v]) stack.push_back({v, u, d + 1});
    }
    blocked[centroid] = 1;
    for (int v : g[centroid])
      if (!blocked[v]) decompose(v, centroid);
  };
  decompose(0, -1);
  vector<multiset<int>> distances(n);
  while (q--) {
    char type;
    int u;
    cin >> type >> u;
    --u;
    if (type == 'T') {
      active[u] ^= 1;
      for (auto [c, d] : path[u]) {
        if (active[u])
          distances[c].insert(d);
        else
          distances[c].erase(distances[c].find(d));
      }
    } else {
      int answer = INT_MAX;
      for (auto [c, d] : path[u])
        if (!distances[c].empty()) answer = min(answer, d + *distances[c].begin());
      cout << (answer == INT_MAX ? -1 : answer) << '\n';
    }
  }
}
