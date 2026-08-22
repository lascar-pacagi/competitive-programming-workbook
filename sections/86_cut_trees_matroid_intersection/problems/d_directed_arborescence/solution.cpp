#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct Edge {
  int u, v;
  ll w;
};
optional<ll> arbo(int n, int root, vector<Edge> e) {
  ll ans = 0;
  while (1) {
    vector<ll> in(n, 4e18);
    vector<int> pre(n, -1);
    for (auto x : e)
      if (x.u != x.v && x.w < in[x.v])
        in[x.v] = x.w, pre[x.v] = x.u;
    in[root] = 0;
    for (ll x : in)
      if (x == 4e18)
        return {};
    for (ll x : in)
      ans += x;
    vector<int> id(n, -1), seen(n, -1);
    int count = 0;
    for (int s = 0; s < n; s++) {
      int v = s;
      while (seen[v] != s && id[v] < 0 && v != root)
        seen[v] = s, v = pre[v];
      if (v != root && id[v] < 0) {
        for (int u = pre[v]; u != v; u = pre[u])
          id[u] = count;
        id[v] = count++;
      }
    }
    if (!count)
      return ans;
    for (int v = 0; v < n; v++)
      if (id[v] < 0)
        id[v] = count++;
    vector<Edge> next;
    for (auto x : e)
      next.push_back({id[x.u], id[x.v], x.w - in[x.v]});
    root = id[root];
    n = count;
    e.swap(next);
  }
};
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m, r;
  cin >> n >> m >> r;
  vector<Edge> e(m);
  for (auto &x : e)
    cin >> x.u >> x.v >> x.w, --x.u, --x.v;
  auto ans = arbo(n, r - 1, e);
  if (ans)
    cout << *ans << '\n';
  else
    cout << "IMPOSSIBLE\n";
}