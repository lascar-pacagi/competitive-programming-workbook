#include <bits/stdc++.h>
using namespace std;
struct DSU {
  vector<int> p;
  DSU(int n) : p(n) { iota(p.begin(), p.end(), 0); }
  int f(int x) { return p[x] == x ? x : p[x] = f(p[x]); }
  bool add(int a, int b) {
    a = f(a);
    b = f(b);
    if (a == b)
      return 0;
    p[a] = b;
    return 1;
  }
};
bool forest_ok(int n, const vector<pair<int, int>> &e, const vector<char> &in) {
  DSU d(n);
  for (int i = 0; i < (int)e.size(); i++)
    if (in[i] && !d.add(e[i].first, e[i].second))
      return 0;
  return 1;
}
vector<char> intersect(int m, function<bool(const vector<char> &)> ok1,
                       function<bool(const vector<char> &)> ok2) {
  vector<char> in(m);
  while (1) {
    vector<int> par(m, -2), q;
    for (int e = 0; e < m; e++)
      if (!in[e]) {
        in[e] = 1;
        bool ok = ok1(in);
        in[e] = 0;
        if (ok)
          par[e] = -1, q.push_back(e);
      }
    int finish = -1;
    for (int h = 0; h < (int)q.size() && finish < 0; h++) {
      int x = q[h];
      if (!in[x]) {
        in[x] = 1;
        bool sink = ok2(in);
        in[x] = 0;
        if (sink) {
          finish = x;
          break;
        }
        for (int y = 0; y < m; y++)
          if (in[y] && par[y] == -2) {
            in[y] = 0;
            in[x] = 1;
            bool ok = ok2(in);
            in[x] = 0;
            in[y] = 1;
            if (ok)
              par[y] = x, q.push_back(y);
          }
      } else
        for (int e = 0; e < m; e++)
          if (!in[e] && par[e] == -2) {
            in[x] = 0;
            in[e] = 1;
            bool ok = ok1(in);
            in[e] = 0;
            in[x] = 1;
            if (ok)
              par[e] = x, q.push_back(e);
          }
    }
    if (finish < 0)
      return in;
    for (int x = finish; x >= 0; x = par[x])
      in[x] ^= 1;
  }
};
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n1, n2, m;
  cin >> n1 >> n2 >> m;
  vector<pair<int, int>> a(m), b(m);
  for (int i = 0; i < m; i++)
    cin >> a[i].first >> a[i].second >> b[i].first >> b[i].second, --a[i].first,
        --a[i].second, --b[i].first, --b[i].second;
  auto in = intersect(
      m, [&](auto &s) { return forest_ok(n1, a, s); },
      [&](auto &s) { return forest_ok(n2, b, s); });
  cout << count(in.begin(), in.end(), 1) << '\n';
}