#include <bits/stdc++.h>
using namespace std;
constexpr long long MOD = 998244353;
struct Function {
  long long a = 1, b = 0;
};
Function then(Function first, Function second) {
  return {second.a * first.a % MOD, (second.a * first.b + second.b) % MOD};
}
struct Aggregate {
  Function forward, backward;
};
Aggregate merge(Aggregate left, Aggregate right) {
  return {then(left.forward, right.forward), then(right.backward, left.backward)};
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  if (!(cin >> n >> q)) return 0;
  vector<Function> fn(n);
  for (auto& f : fn) cin >> f.a >> f.b;
  vector<vector<int>> g(n);
  for (int i = 1, u, v; i < n; i++) {
    cin >> u >> v;
    --u;
    --v;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  vector<int> parent(n, -1), depth(n), order{0};
  for (int i = 0; i < (int)order.size(); i++) {
    int u = order[i];
    for (int v : g[u])
      if (v != parent[u]) parent[v] = u, depth[v] = depth[u] + 1, order.push_back(v);
  }
  vector<int> size(n, 1), heavy(n, -1);
  for (int i = n - 1; i > 0; i--) {
    int u = order[i], p = parent[u];
    size[p] += size[u];
    if (heavy[p] < 0 || size[u] > size[heavy[p]]) heavy[p] = u;
  }
  vector<int> head(n), position(n);
  int timer = 0;
  vector<pair<int, int>> chains{{0, 0}};
  while (!chains.empty()) {
    auto [start, h] = chains.back();
    chains.pop_back();
    for (int u = start; u != -1; u = heavy[u]) {
      head[u] = h;
      position[u] = timer++;
      for (int v : g[u])
        if (parent[v] == u && v != heavy[u]) chains.push_back({v, v});
    }
  }
  int base = 1;
  while (base < n) base *= 2;
  vector<Aggregate> tree(2 * base);
  for (int u = 0; u < n; u++) tree[base + position[u]] = {fn[u], fn[u]};
  for (int i = base - 1; i; i--) tree[i] = merge(tree[2 * i], tree[2 * i + 1]);
  auto range = [&](int l, int r) {
    Aggregate left{}, right{};
    for (l += base, r += base + 1; l < r; l /= 2, r /= 2) {
      if (l & 1) left = merge(left, tree[l++]);
      if (r & 1) right = merge(tree[--r], right);
    }
    return merge(left, right);
  };
  while (q--) {
    char type;
    cin >> type;
    if (type == 'U') {
      int u;
      Function f;
      cin >> u >> f.a >> f.b;
      --u;
      int p = base + position[u];
      tree[p] = {f, f};
      for (p /= 2; p; p /= 2) tree[p] = merge(tree[2 * p], tree[2 * p + 1]);
    } else {
      int u, v;
      long long x;
      cin >> u >> v >> x;
      --u;
      --v;
      Function left{}, right{};
      while (head[u] != head[v]) {
        if (depth[head[u]] >= depth[head[v]]) {
          left = then(left, range(position[head[u]], position[u]).backward);
          u = parent[head[u]];
        } else {
          right = then(range(position[head[v]], position[v]).forward, right);
          v = parent[head[v]];
        }
      }
      Function middle = position[u] <= position[v]
                            ? range(position[u], position[v]).forward
                            : range(position[v], position[u]).backward;
      Function all = then(then(left, middle), right);
      cout << (all.a * x + all.b) % MOD << '\n';
    }
  }
}
