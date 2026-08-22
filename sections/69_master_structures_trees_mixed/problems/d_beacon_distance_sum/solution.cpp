#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
struct Entry {
  int centroid, distance, branch;
};
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
  vector<int> subtree(n);
  vector<int> traversal_parent(n), seen(n);
  int stamp = 0;
  vector<vector<Entry>> path(n);
  vector<int> todo{0};
  while (!todo.empty()) {
    int entry = todo.back();
    todo.pop_back();
    ++stamp;
    vector<int> nodes{entry};
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
    path[centroid].push_back({centroid, 0, -1});
    for (int first : g[centroid])
      if (!blocked[first]) {
        vector<tuple<int, int, int>> stack{{first, centroid, 1}};
        while (!stack.empty()) {
          auto [u, p, d] = stack.back();
          stack.pop_back();
          path[u].push_back({centroid, d, first});
          for (int v : g[u])
            if (v != p && !blocked[v]) stack.push_back({v, u, d + 1});
        }
      }
    blocked[centroid] = 1;
    for (int v : g[centroid])
      if (!blocked[v]) todo.push_back(v);
  }
  vector<int64> count(n), sum(n);
  unordered_map<long long, pair<int64, int64>> excluded;
  auto key = [&](int c, int b) { return 1LL * c * n + b; };
  while (q--) {
    char type;
    int u;
    cin >> type >> u;
    --u;
    if (type == 'T') {
      int delta = active[u] ? -1 : 1;
      active[u] ^= 1;
      for (auto [c, d, b] : path[u]) {
        count[c] += delta;
        sum[c] += 1LL * delta * d;
        if (b != -1) {
          auto& state = excluded[key(c, b)];
          state.first += delta;
          state.second += 1LL * delta * d;
        }
      }
    } else {
      int64 answer = 0;
      for (auto [c, d, b] : path[u]) {
        answer += sum[c] + count[c] * d;
        if (b != -1) {
          auto state = excluded[key(c, b)];
          answer -= state.second + state.first * d;
        }
      }
      cout << answer << '\n';
    }
  }
}
