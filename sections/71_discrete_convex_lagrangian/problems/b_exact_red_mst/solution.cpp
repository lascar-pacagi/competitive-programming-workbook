#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
struct DSU {
  vector<int> p, sz;
  DSU(int n) : p(n), sz(n, 1) { iota(p.begin(), p.end(), 0); }
  int find(int x) {
    while (x != p[x])
      x = p[x];
    return x;
  }
  bool unite(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b)
      return false;
    if (sz[a] < sz[b])
      swap(a, b);
    p[b] = a;
    sz[a] += sz[b];
    return true;
  }
};
struct Edge {
  int u, v, red;
  int64 w;
};
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m, wanted;
  if (!(cin >> n >> m >> wanted))
    return 0;
  vector<Edge> edges(m);
  for (auto &e : edges) {
    char c;
    cin >> e.u >> e.v >> e.w >> c;
    --e.u;
    --e.v;
    e.red = c == 'R';
  }
  auto run = [&](int64 lambda, bool prefer_red) {
    vector<int> order(m);
    iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(), [&](int i, int j) {
      int64 a = edges[i].w + lambda * edges[i].red;
      int64 b = edges[j].w + lambda * edges[j].red;
      if (a != b)
        return a < b;
      return prefer_red ? edges[i].red > edges[j].red
                        : edges[i].red < edges[j].red;
    });
    DSU dsu(n);
    int used = 0, red = 0;
    int64 value = 0;
    for (int id : order)
      if (dsu.unite(edges[id].u, edges[id].v)) {
        ++used;
        red += edges[id].red;
        value += edges[id].w + lambda * edges[id].red;
      }
    return tuple<int, int, int64>{used, red, value};
  };
  auto [u1, min_red, z1] = run(400000000000000LL, false);
  auto [u2, max_red, z2] = run(-400000000000000LL, true);
  if (u1 != n - 1 || wanted < min_red || wanted > max_red) {
    cout << "IMPOSSIBLE\n";
    return 0;
  }
  int64 lo = -400000000000000LL, hi = 400000000000000LL;
  while (lo < hi) {
    int64 mid = lo + (hi - lo + 1) / 2;
    auto [used, red, value] = run(mid, true);
    if (red >= wanted)
      lo = mid;
    else
      hi = mid - 1;
  }
  auto [used, red, modified] = run(lo, true);
  cout << modified - lo * wanted << '\n';
}
