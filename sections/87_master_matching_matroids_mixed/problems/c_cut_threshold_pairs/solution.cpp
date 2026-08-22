#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct Dinic {
  struct E {
    int v, rev;
    ll c;
  };
  int n;
  vector<vector<E>> g;
  vector<int> level, it;
  vector<char> side;
  Dinic(int n) : n(n), g(n), level(n), it(n), side(n) {}
  void add(int u, int v, ll c) {
    g[u].push_back({v, (int)g[v].size(), c});
    g[v].push_back({u, (int)g[u].size() - 1, 0});
  }
  ll dfs(int u, int t, ll f) {
    if (u == t)
      return f;
    for (int &i = it[u]; i < (int)g[u].size(); i++) {
      E &e = g[u][i];
      if (e.c && level[e.v] == level[u] + 1) {
        ll z = dfs(e.v, t, min(f, e.c));
        if (z) {
          e.c -= z;
          g[e.v][e.rev].c += z;
          return z;
        }
      }
    }
    return 0;
  }
  ll flow(int s, int t) {
    ll ans = 0;
    while (1) {
      fill(level.begin(), level.end(), -1);
      queue<int> q;
      q.push(s);
      level[s] = 0;
      while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (auto &e : g[u])
          if (e.c && level[e.v] < 0)
            level[e.v] = level[u] + 1, q.push(e.v);
      }
      if (level[t] < 0) {
        for (int i = 0; i < n; i++)
          side[i] = level[i] >= 0;
        return ans;
      }
      fill(it.begin(), it.end(), 0);
      while (ll z = dfs(s, t, 4e18))
        ans += z;
    }
  }
};
vector<vector<pair<int, ll>>> gomory(int n, vector<tuple<int, int, ll>> e) {
  vector<int> p(n);
  vector<ll> w(n);
  for (int s = 1; s < n; s++) {
    int t = p[s];
    Dinic d(n);
    for (auto [u, v, c] : e)
      d.add(u, v, c), d.add(v, u, c);
    w[s] = d.flow(s, t);
    for (int v = s + 1; v < n; v++)
      if (p[v] == t && d.side[v])
        p[v] = s;
    if (d.side[p[t]])
      p[s] = p[t], p[t] = s, swap(w[s], w[t]);
  }
  vector<vector<pair<int, ll>>> tree(n);
  for (int v = 1; v < n; v++)
    tree[v].push_back({p[v], w[v]}), tree[p[v]].push_back({v, w[v]});
  return tree;
}
struct MinTree {
  int n, L;
  vector<int> dep;
  vector<vector<int>> up;
  vector<vector<ll>> mn;
  MinTree(vector<vector<pair<int, ll>>> t)
      : n(t.size()), L(max(1, (int)bit_width((unsigned)n))), dep(n),
        up(L, vector<int>(n)), mn(L, vector<ll>(n, 4e18)) {
    vector<pair<int, int>> st = {{0, 0}};
    while (!st.empty()) {
      auto [u, p] = st.back();
      st.pop_back();
      up[0][u] = p;
      for (auto [v, w] : t[u])
        if (v != p)
          dep[v] = dep[u] + 1, mn[0][v] = w, st.push_back({v, u});
    }
    for (int j = 1; j < L; j++)
      for (int v = 0; v < n; v++)
        mn[j][v] = min(mn[j - 1][v], mn[j - 1][up[j - 1][v]]),
        up[j][v] = up[j - 1][up[j - 1][v]];
  }
  ll query(int a, int b) {
    ll ans = 4e18;
    if (dep[a] < dep[b])
      swap(a, b);
    int z = dep[a] - dep[b];
    for (int j = 0; j < L; j++)
      if (z >> j & 1)
        ans = min(ans, mn[j][a]), a = up[j][a];
    if (a == b)
      return ans;
    for (int j = L - 1; j >= 0; j--)
      if (up[j][a] != up[j][b])
        ans = min({ans, mn[j][a], mn[j][b]}), a = up[j][a], b = up[j][b];
    return min({ans, mn[0][a], mn[0][b]});
  }
};
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m, q;
  cin >> n >> m >> q;
  vector<tuple<int, int, ll>> e(m);
  for (auto &[u, v, c] : e)
    cin >> u >> v >> c, --u, --v;
  MinTree t(gomory(n, e));
  vector<ll> a;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < i; j++)
      a.push_back(t.query(i, j));
  sort(a.begin(), a.end());
  while (q--) {
    ll x;
    cin >> x;
    cout << upper_bound(a.begin(), a.end(), x) - a.begin() << '\n';
  }
}