#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct E {
  int to, rev, cap;
  ll cost;
};
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m, k;
  if (!(cin >> n >> m >> k))
    return 0;
  vector<vector<E>> g(n);
  auto add = [&](int u, int v, ll c) {
    g[u].push_back({v, (int)g[v].size(), 1, c});
    g[v].push_back({u, (int)g[u].size() - 1, 0, -c});
  };
  while (m--) {
    int u, v;
    ll p;
    cin >> u >> v >> p;
    add(u - 1, v - 1, -p);
  }
  ll cost = 0;
  int flow = 0;
  const ll INF = 4e18;
  while (flow < k) {
    vector<ll> d(n, INF);
    vector<int> pv(n), pe(n);
    vector<char> in(n);
    queue<int> q;
    d[0] = 0;
    q.push(0);
    in[0] = 1;
    while (!q.empty()) {
      int u = q.front();
      q.pop();
      in[u] = 0;
      for (int i = 0; i < (int)g[u].size(); i++) {
        E &e = g[u][i];
        if (e.cap && d[e.to] > d[u] + e.cost) {
          d[e.to] = d[u] + e.cost;
          pv[e.to] = u;
          pe[e.to] = i;
          if (!in[e.to])
            in[e.to] = 1, q.push(e.to);
        }
      }
    }
    if (d[n - 1] == INF)
      break;
    cost += d[n - 1];
    flow++;
    for (int v = n - 1; v; v = pv[v]) {
      E &e = g[pv[v]][pe[v]];
      e.cap--;
      g[v][e.rev].cap++;
    }
  }
  if (flow < k)
    cout << "IMPOSSIBLE\n";
  else
    cout << -cost << '\n';
}
