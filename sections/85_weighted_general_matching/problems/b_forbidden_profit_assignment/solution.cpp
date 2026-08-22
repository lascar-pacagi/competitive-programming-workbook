#include <bits/stdc++.h>
using namespace std;
using ll = long long;
pair<ll, vector<int>> hungarian(vector<vector<ll>> a) {
  int n = a.size(), m = a[0].size();
  vector<ll> u(n + 1), v(m + 1);
  vector<int> p(m + 1), way(m + 1);
  for (int i = 1; i <= n; i++) {
    p[0] = i;
    int j0 = 0;
    vector<ll> mn(m + 1, 4e18);
    vector<char> used(m + 1);
    do {
      used[j0] = 1;
      int i0 = p[j0], j1 = 0;
      ll delta = 4e18;
      for (int j = 1; j <= m; j++)
        if (!used[j]) {
          ll cur = a[i0 - 1][j - 1] - u[i0] - v[j];
          if (cur < mn[j])
            mn[j] = cur, way[j] = j0;
          if (mn[j] < delta)
            delta = mn[j], j1 = j;
        }
      for (int j = 0; j <= m; j++)
        if (used[j])
          u[p[j]] += delta, v[j] -= delta;
        else
          mn[j] -= delta;
      j0 = j1;
    } while (p[j0]);
    do {
      int j1 = way[j0];
      p[j0] = p[j1];
      j0 = j1;
    } while (j0);
  }
  vector<int> match(n);
  for (int j = 1; j <= m; j++)
    if (p[j])
      match[p[j] - 1] = j - 1;
  return {-v[0], match};
}
struct Blossom {
  int n;
  vector<vector<int>> g;
  vector<int> match, p, base, q;
  vector<char> used, flower;
  Blossom(vector<vector<int>> g)
      : n(g.size()), g(g), match(n, -1), p(n), base(n), q(n), used(n),
        flower(n) {}
  int lca(int a, int b) {
    vector<char> mark(n);
    while (1) {
      a = base[a];
      mark[a] = 1;
      if (match[a] < 0)
        break;
      a = p[match[a]];
    }
    while (1) {
      b = base[b];
      if (mark[b])
        return b;
      b = p[match[b]];
    }
  }
  void mark_path(int v, int b, int child) {
    while (base[v] != b) {
      flower[base[v]] = flower[base[match[v]]] = 1;
      p[v] = child;
      child = match[v];
      v = p[match[v]];
    }
  }
  int path(int root) {
    fill(used.begin(), used.end(), 0);
    fill(p.begin(), p.end(), -1);
    iota(base.begin(), base.end(), 0);
    int qh = 0, qt = 0;
    q[qt++] = root;
    used[root] = 1;
    while (qh < qt) {
      int v = q[qh++];
      for (int u : g[v])
        if (base[v] != base[u] && match[v] != u) {
          if (u == root || (match[u] >= 0 && p[match[u]] >= 0)) {
            int b = lca(v, u);
            fill(flower.begin(), flower.end(), 0);
            mark_path(v, b, u);
            mark_path(u, b, v);
            for (int x = 0; x < n; x++)
              if (flower[base[x]]) {
                base[x] = b;
                if (!used[x])
                  used[x] = 1, q[qt++] = x;
              }
          } else if (p[u] < 0) {
            p[u] = v;
            if (match[u] < 0)
              return u;
            u = match[u];
            used[u] = 1;
            q[qt++] = u;
          }
        }
    }
    return -1;
  }
  int solve() {
    for (int root = 0; root < n; root++)
      if (match[root] < 0) {
        int v = path(root);
        while (v >= 0) {
          int pv = p[v], nv = pv < 0 ? -1 : match[pv];
          match[v] = pv;
          if (pv >= 0)
            match[pv] = v;
          v = nv;
        }
      }
    return count_if(match.begin(), match.end(), [](int x) { return x >= 0; }) /
           2;
  }
};
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  const ll X = 1e15;
  vector<vector<ll>> a(n, vector<ll>(m));
  for (auto &r : a)
    for (auto &x : r) {
      cin >> x;
      x = x < 0 ? X : -x;
    }
  auto [cost, match] = hungarian(a);
  for (int i = 0; i < n; i++)
    if (a[i][match[i]] >= X) {
      cout << "IMPOSSIBLE\n";
      return 0;
    }
  cout << -cost << '\n';
}