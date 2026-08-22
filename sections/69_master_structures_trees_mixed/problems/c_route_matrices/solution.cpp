#include <bits/stdc++.h>
using namespace std;
constexpr long long MOD = 998244353;
struct Matrix {
  long long a = 1, b = 0, c = 0, d = 1;
};
Matrix multiply(Matrix x, Matrix y) {
  return {(x.a * y.a + x.b * y.c) % MOD, (x.a * y.b + x.b * y.d) % MOD,
          (x.c * y.a + x.d * y.c) % MOD, (x.c * y.b + x.d * y.d) % MOD};
}
struct Item {
  Matrix forward, backward;
};
Item merge(Item x, Item y) {
  return {multiply(x.forward, y.forward), multiply(y.backward, x.backward)};
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  if (!(cin >> n >> q)) return 0;
  vector<Matrix> value(n);
  for (auto& m : value) cin >> m.a >> m.b >> m.c >> m.d;
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
  for (int i = n - 1; i; i--) {
    int u = order[i], p = parent[u];
    size[p] += size[u];
    if (heavy[p] < 0 || size[u] > size[heavy[p]]) heavy[p] = u;
  }
  vector<int> head(n), pos(n);
  int timer = 0;
  vector<pair<int, int>> todo{{0, 0}};
  while (!todo.empty()) {
    auto [u, h] = todo.back();
    todo.pop_back();
    for (; u != -1; u = heavy[u]) {
      head[u] = h;
      pos[u] = timer++;
      for (int v : g[u])
        if (parent[v] == u && v != heavy[u]) todo.push_back({v, v});
    }
  }
  int base = 1;
  while (base < n) base *= 2;
  vector<Item> tree(2 * base);
  for (int u = 0; u < n; u++) tree[base + pos[u]] = {value[u], value[u]};
  for (int p = base - 1; p; p--) tree[p] = merge(tree[2 * p], tree[2 * p + 1]);
  auto range = [&](int l, int r) {
    Item x{}, y{};
    for (l += base, r += base + 1; l < r; l /= 2, r /= 2) {
      if (l & 1) x = merge(x, tree[l++]);
      if (r & 1) y = merge(tree[--r], y);
    }
    return merge(x, y);
  };
  while (q--) {
    char type;
    int u;
    cin >> type >> u;
    --u;
    if (type == 'U') {
      Matrix m;
      cin >> m.a >> m.b >> m.c >> m.d;
      int p = base + pos[u];
      tree[p] = {m, m};
      for (p /= 2; p; p /= 2) tree[p] = merge(tree[2 * p], tree[2 * p + 1]);
    } else {
      int v;
      cin >> v;
      --v;
      Matrix left{}, right{};
      while (head[u] != head[v]) {
        if (depth[head[u]] >= depth[head[v]])
          left = multiply(left, range(pos[head[u]], pos[u]).backward),
          u = parent[head[u]];
        else
          right = multiply(range(pos[head[v]], pos[v]).forward, right),
          v = parent[head[v]];
      }
      Matrix middle = pos[u] <= pos[v] ? range(pos[u], pos[v]).forward
                                       : range(pos[v], pos[u]).backward;
      Matrix answer = multiply(multiply(left, middle), right);
      cout << answer.a << ' ' << answer.b << ' ' << answer.c << ' ' << answer.d << '\n';
    }
  }
}
