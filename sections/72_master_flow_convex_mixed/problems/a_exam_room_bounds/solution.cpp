#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

struct Dinic {
  struct Edge {
    int to, rev;
    int64 cap;
  };
  vector<vector<Edge>> g;
  vector<int> level, it;
  Dinic(int n) : g(n), level(n), it(n) {}
  void add_edge(int u, int v, int64 cap) {
    Edge a{v, (int)g[v].size(), cap};
    Edge b{u, (int)g[u].size(), 0};
    g[u].push_back(a);
    g[v].push_back(b);
  }
  bool bfs(int s, int t) {
    fill(level.begin(), level.end(), -1);
    queue<int> q;
    level[s] = 0;
    q.push(s);
    while (!q.empty()) {
      int u = q.front();
      q.pop();
      for (auto &e : g[u])
        if (e.cap && level[e.to] < 0)
          level[e.to] = level[u] + 1, q.push(e.to);
    }
    return level[t] >= 0;
  }
  int64 dfs(int u, int t, int64 pushed) {
    if (u == t)
      return pushed;
    for (int &i = it[u]; i < (int)g[u].size(); ++i) {
      Edge &e = g[u][i];
      if (!e.cap || level[e.to] != level[u] + 1)
        continue;
      int64 take = dfs(e.to, t, min(pushed, e.cap));
      if (take) {
        e.cap -= take;
        g[e.to][e.rev].cap += take;
        return take;
      }
    }
    return 0;
  }
  int64 flow(int s, int t) {
    int64 ans = 0, pushed;
    while (bfs(s, t)) {
      fill(it.begin(), it.end(), 0);
      while ((pushed = dfs(s, t, (1LL << 62))))
        ans += pushed;
    }
    return ans;
  }
};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int rows, cols, m;
  if (!(cin >> rows >> cols >> m))
    return 0;
  int n = rows + cols + 2;
  int source = rows + cols, sink = source + 1, ss = n, tt = n + 1;
  Dinic dinic(n + 2);
  vector<int64> balance(n);
  int64 total = 0;
  auto bounded = [&](int u, int v, int64 low, int64 high) {
    dinic.add_edge(u, v, high - low);
    balance[u] -= low;
    balance[v] += low;
  };
  for (int i = 0; i < rows; ++i) {
    int64 demand;
    cin >> demand;
    bounded(source, i, demand, demand);
    total += demand;
  }
  for (int j = 0; j < cols; ++j) {
    int64 low, high;
    cin >> low >> high;
    bounded(rows + j, sink, low, high);
  }
  for (int i = 0, r, c; i < m; ++i) {
    cin >> r >> c;
    bounded(--r, rows + --c, 0, 1);
  }
  bounded(sink, source, total, total);
  int64 need = 0;
  for (int v = 0; v < n; ++v) {
    if (balance[v] > 0)
      dinic.add_edge(ss, v, balance[v]), need += balance[v];
    if (balance[v] < 0)
      dinic.add_edge(v, tt, -balance[v]);
  }
  cout << (dinic.flow(ss, tt) == need ? "YES\n" : "NO\n");
}
