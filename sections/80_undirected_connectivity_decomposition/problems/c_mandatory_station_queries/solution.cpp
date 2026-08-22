#include <bits/stdc++.h>
using namespace std;
struct SCC {
  int n, c = 0;
  vector<vector<int>> g, rg;
  vector<int> id, order;
  SCC(int n, vector<pair<int, int>> e) : n(n), g(n), rg(n), id(n, -1) {
    for (auto [u, v] : e)
      g[u].push_back(v), rg[v].push_back(u);
    vector<char> seen(n);
    for (int s = 0; s < n; s++)
      if (!seen[s]) {
        vector<pair<int, int>> st = {{s, 0}};
        seen[s] = 1;
        while (!st.empty()) {
          auto &[u, i] = st.back();
          if (i < (int)g[u].size()) {
            int v = g[u][i++];
            if (!seen[v])
              seen[v] = 1, st.push_back({v, 0});
          } else
            order.push_back(u), st.pop_back();
        }
      }
    reverse(order.begin(), order.end());
    for (int s : order)
      if (id[s] < 0) {
        id[s] = c;
        vector<int> st = {s};
        while (!st.empty()) {
          int u = st.back();
          st.pop_back();
          for (int v : rg[u])
            if (id[v] < 0)
              id[v] = c, st.push_back(v);
        }
        c++;
      }
  }
};
struct LowLink {
  int n, timer = 0;
  vector<pair<int, int>> e;
  vector<vector<pair<int, int>>> g;
  vector<int> tin, low, sub, parent_edge, it;
  vector<char> bridge;
  vector<vector<int>> parts;
  LowLink(int n, vector<pair<int, int>> e)
      : n(n), e(e), g(n), tin(n, -1), low(n), sub(n), parent_edge(n, -1), it(n),
        bridge(e.size()), parts(n) {
    for (int i = 0; i < (int)e.size(); i++) {
      auto [u, v] = e[i];
      g[u].push_back({v, i});
      g[v].push_back({u, i});
    }
    tin[0] = low[0] = timer++;
    sub[0] = 1;
    vector<int> st = {0};
    while (!st.empty()) {
      int u = st.back();
      if (it[u] < (int)g[u].size()) {
        auto [v, id] = g[u][it[u]++];
        if (id == parent_edge[u])
          continue;
        if (tin[v] >= 0)
          low[u] = min(low[u], tin[v]);
        else {
          parent_edge[v] = id;
          tin[v] = low[v] = timer++;
          sub[v] = 1;
          st.push_back(v);
        }
      } else {
        st.pop_back();
        int id = parent_edge[u];
        if (id < 0)
          continue;
        auto [a, b] = e[id];
        int p = a ^ b ^ u;
        sub[p] += sub[u];
        low[p] = min(low[p], low[u]);
        if (low[u] > tin[p])
          bridge[id] = 1;
        if (low[u] >= tin[p])
          parts[p].push_back(sub[u]);
      }
    }
  }
};
pair<vector<int>, vector<vector<int>>>
bridge_tree(int n, const vector<pair<int, int>> &e) {
  LowLink l(n, e);
  vector<int> id(n, -1);
  int c = 0;
  for (int s = 0; s < n; s++)
    if (id[s] < 0) {
      id[s] = c;
      vector<int> st = {s};
      while (!st.empty()) {
        int u = st.back();
        st.pop_back();
        for (auto [v, k] : l.g[u])
          if (!l.bridge[k] && id[v] < 0)
            id[v] = c, st.push_back(v);
      }
      c++;
    }
  vector<vector<int>> t(c);
  for (int i = 0; i < (int)e.size(); i++)
    if (l.bridge[i]) {
      auto [u, v] = e[i];
      u = id[u];
      v = id[v];
      t[u].push_back(v);
      t[v].push_back(u);
    }
  return {id, t};
}
struct TreeDistance {
  int n, L;
  vector<int> d;
  vector<vector<int>> up;
  TreeDistance(vector<vector<int>> t)
      : n(t.size()), L(max(1, (int)bit_width((unsigned)max(1, n)))), d(n),
        up(L, vector<int>(n)) {
    vector<pair<int, int>> st = {{0, 0}};
    while (!st.empty()) {
      auto [u, p] = st.back();
      st.pop_back();
      up[0][u] = p;
      for (int v : t[u])
        if (v != p)
          d[v] = d[u] + 1, st.push_back({v, u});
    }
    for (int j = 1; j < L; j++)
      for (int i = 0; i < n; i++)
        up[j][i] = up[j - 1][up[j - 1][i]];
  }
  int lca(int a, int b) {
    if (d[a] < d[b])
      swap(a, b);
    int z = d[a] - d[b];
    for (int j = 0; j < L; j++)
      if (z >> j & 1)
        a = up[j][a];
    if (a == b)
      return a;
    for (int j = L - 1; j >= 0; j--)
      if (up[j][a] != up[j][b])
        a = up[j][a], b = up[j][b];
    return up[0][a];
  }
  int dist(int a, int b) {
    int c = lca(a, b);
    return d[a] + d[b] - 2 * d[c];
  }
};
vector<vector<int>> block_cut(int n, const vector<pair<int, int>> &e) {
  vector<vector<pair<int, int>>> g(n);
  for (int i = 0; i < (int)e.size(); i++) {
    auto [u, v] = e[i];
    g[u].push_back({v, i});
    g[v].push_back({u, i});
  }
  vector<int> tin(n, -1), low(n), edges, parent(n, -1), it(n);
  vector<vector<int>> t(n);
  int timer = 0;
  tin[0] = low[0] = timer++;
  vector<int> dfs = {0};
  while (!dfs.empty()) {
    int u = dfs.back();
    if (it[u] < (int)g[u].size()) {
      auto [v, id] = g[u][it[u]++];
      if (id == parent[u])
        continue;
      if (tin[v] < 0) {
        parent[v] = id;
        edges.push_back(id);
        tin[v] = low[v] = timer++;
        dfs.push_back(v);
      } else if (tin[v] < tin[u])
        edges.push_back(id), low[u] = min(low[u], tin[v]);
    } else {
      dfs.pop_back();
      int id = parent[u];
      if (id < 0)
        continue;
      auto [a, b] = e[id];
      int p = a ^ b ^ u;
      low[p] = min(low[p], low[u]);
      if (low[u] >= tin[p]) {
        vector<int> vs;
        while (1) {
          int x = edges.back();
          edges.pop_back();
          vs.push_back(e[x].first);
          vs.push_back(e[x].second);
          if (x == id)
            break;
        }
        sort(vs.begin(), vs.end());
        vs.erase(unique(vs.begin(), vs.end()), vs.end());
        int block = t.size();
        t.push_back({});
        for (int x : vs)
          t[block].push_back(x), t[x].push_back(block);
      }
    }
  }
  return t;
}
vector<bitset<1500>> dominators(int n, const vector<pair<int, int>> &e) {
  vector<vector<int>> g(n), pred(n);
  for (auto [u, v] : e)
    g[u].push_back(v), pred[v].push_back(u);
  bitset<1500> reach;
  reach[0] = 1;
  vector<int> st = {0};
  while (!st.empty()) {
    int u = st.back();
    st.pop_back();
    for (int v : g[u])
      if (!reach[v])
        reach[v] = 1, st.push_back(v);
  }
  vector<bitset<1500>> d(n, reach);
  d[0].reset();
  d[0][0] = 1;
  bool change = 1;
  while (change) {
    change = 0;
    for (int v = 1; v < n; v++)
      if (reach[v]) {
        bitset<1500> x = reach;
        for (int p : pred[v])
          if (reach[p])
            x &= d[p];
        x[v] = 1;
        if (x != d[v])
          d[v] = x, change = 1;
      }
  }
  return d;
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m, q;
  cin >> n >> m >> q;
  vector<pair<int, int>> e(m);
  for (auto &[u, v] : e)
    cin >> u >> v, --u, --v;
  TreeDistance d(block_cut(n, e));
  while (q--) {
    int u, v, c;
    cin >> u >> v >> c;
    --u;
    --v;
    --c;
    cout << (d.dist(u, v) == d.dist(u, c) + d.dist(c, v) ? "YES\n" : "NO\n");
  }
}