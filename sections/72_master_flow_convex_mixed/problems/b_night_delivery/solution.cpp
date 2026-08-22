#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
const int64 INF = (1LL << 62);

struct MCF {
  struct Edge {
    int to, rev, cap, initial;
    int64 cost;
  };
  vector<vector<Edge>> g;
  MCF(int n) : g(n) {}
  pair<int, int> add_edge(int u, int v, int cap, int64 cost) {
    int id = g[u].size();
    g[u].push_back({v, (int)g[v].size(), cap, cap, cost});
    g[v].push_back({u, id, 0, 0, -cost});
    return {u, id};
  }
  pair<int, int64> flow(int s, int t, int limit) {
    int n = g.size(), sent = 0;
    int64 cost = 0;
    vector<int64> pot(n, INF), dist(n);
    pot[s] = 0;
    for (int rep = 0; rep < n; ++rep) {
      bool changed = false;
      for (int u = 0; u < n; ++u)
        if (pot[u] < INF)
          for (auto &e : g[u])
            if (e.cap && pot[e.to] > pot[u] + e.cost)
              pot[e.to] = pot[u] + e.cost, changed = true;
      if (!changed)
        break;
    }
    for (auto &x : pot)
      if (x == INF)
        x = 0;
    vector<int> pv(n), pe(n);
    while (sent < limit) {
      fill(dist.begin(), dist.end(), INF);
      dist[s] = 0;
      priority_queue<pair<int64, int>, vector<pair<int64, int>>,
                     greater<pair<int64, int>>>
          pq;
      pq.push({0, s});
      while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (d != dist[u])
          continue;
        for (int i = 0; i < (int)g[u].size(); ++i) {
          auto &e = g[u][i];
          int64 nd = d + e.cost + pot[u] - pot[e.to];
          if (e.cap && nd < dist[e.to])
            dist[e.to] = nd, pv[e.to] = u, pe[e.to] = i, pq.push({nd, e.to});
        }
      }
      if (dist[t] == INF)
        break;
      for (int v = 0; v < n; ++v)
        if (dist[v] < INF)
          pot[v] += dist[v];
      int add = limit - sent;
      for (int v = t; v != s; v = pv[v])
        add = min(add, g[pv[v]][pe[v]].cap);
      for (int v = t; v != s; v = pv[v]) {
        Edge &e = g[pv[v]][pe[v]];
        cost += (int64)add * e.cost;
        e.cap -= add;
        g[v][e.rev].cap += add;
      }
      sent += add;
    }
    return {sent, cost};
  }
};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m, need;
  if (!(cin >> n >> m >> need))
    return 0;
  int s, t;
  cin >> s >> t;
  --s;
  --t;
  MCF mcf(n);
  for (int i = 0, u, v, cap; i < m; ++i) {
    int64 cost;
    cin >> u >> v >> cap >> cost;
    mcf.add_edge(--u, --v, cap, cost);
  }
  auto [sent, cost] = mcf.flow(s, t, need);
  if (sent < need)
    cout << "IMPOSSIBLE\n";
  else
    cout << cost << '\n';
}
