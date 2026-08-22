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
int locate(const vector<P> &p, P q) {
  int n = p.size();
  if (n == 1)
    return q == p[0] ? 0 : -1;
  if (n == 2)
    return cross(p[0], p[1], q) == 0 && min(p[0].x, p[1].x) <= q.x &&
                   q.x <= max(p[0].x, p[1].x) && min(p[0].y, p[1].y) <= q.y &&
                   q.y <= max(p[0].y, p[1].y)
               ? 0
               : -1;
  long long a = cross(p[0], p[1], q), b = cross(p[0], p.back(), q);
  if (a < 0 || b > 0)
    return -1;
  if (a == 0)
    return dist2(p[0], q) <= dist2(p[0], p[1]) ? 0 : -1;
  if (b == 0)
    return dist2(p[0], q) <= dist2(p[0], p.back()) ? 0 : -1;
  int l = 1, r = n - 1;
  while (r - l > 1) {
    int mid = (l + r) / 2;
    if (cross(p[0], p[mid], q) >= 0)
      l = mid;
    else
      r = mid;
  }
  long long z = cross(p[l], p[(l + 1) % n], q);
  return z < 0 ? -1 : (z == 0 ? 0 : 1);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  if (!(cin >> n >> q))
    return 0;
  vector<P> p(n);
  for (auto &x : p)
    cin >> x.x >> x.y;
  auto h = hull(p);
  while (q--) {
    P x;
    cin >> x.x >> x.y;
    int z = locate(h, x);
    cout << (z < 0 ? "OUT\n" : z == 0 ? "BOUNDARY\n" : "IN\n");
  }
}
