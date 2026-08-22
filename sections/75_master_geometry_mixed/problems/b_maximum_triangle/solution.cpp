#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
struct P {
  int64 x, y;
};
bool operator<(P a, P b) { return tie(a.x, a.y) < tie(b.x, b.y); }
bool operator==(P a, P b) { return a.x == b.x && a.y == b.y; }
P operator+(P a, P b) { return {a.x + b.x, a.y + b.y}; }
P operator-(P a, P b) { return {a.x - b.x, a.y - b.y}; }
int64 cross(P a, P b) { return a.x * b.y - a.y * b.x; }
int64 cross(P a, P b, P c) { return cross(b - a, c - a); }
int64 dist2(P a, P b) {
  int64 x = a.x - b.x, y = a.y - b.y;
  return x * x + y * y;
}
vector<P> hull(vector<P> p) {
  sort(p.begin(), p.end());
  p.erase(unique(p.begin(), p.end()), p.end());
  if (p.size() <= 1)
    return p;
  vector<P> h;
  for (P x : p) {
    while (h.size() >= 2 && cross(h[h.size() - 2], h.back(), x) <= 0)
      h.pop_back();
    h.push_back(x);
  }
  size_t lower = h.size();
  for (int i = (int)p.size() - 2; i >= 0; --i) {
    P x = p[i];
    while (h.size() > lower && cross(h[h.size() - 2], h.back(), x) <= 0)
      h.pop_back();
    h.push_back(x);
  }
  h.pop_back();
  return h;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  if (!(cin >> n))
    return 0;
  vector<P> p(n);
  for (auto &q : p)
    cin >> q.x >> q.y;
  auto h = hull(p);
  int m = h.size();
  long long ans = 0;
  for (int i = 0; i < m; ++i) {
    int k = i + 2;
    for (int j = i + 1; j < m; ++j) {
      if (k <= j)
        k = j + 1;
      if (k >= m)
        break;
      while (k + 1 < m && llabs(cross(h[i], h[j], h[k + 1])) >
                              llabs(cross(h[i], h[j], h[k])))
        ++k;
      ans = max(ans, llabs(cross(h[i], h[j], h[k])));
    }
  }
  cout << ans << '\n';
}
