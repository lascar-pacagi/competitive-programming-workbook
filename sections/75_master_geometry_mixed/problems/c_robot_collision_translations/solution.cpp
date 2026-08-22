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

vector<P> normalize(vector<P> p) {
  if (p.size() <= 1)
    return p;
  if (cross(p[0], p[1], p[2]) < 0)
    reverse(p.begin(), p.end());
  int at = min_element(p.begin(), p.end(),
                       [](P a, P b) { return tie(a.y, a.x) < tie(b.y, b.x); }) -
           p.begin();
  rotate(p.begin(), p.begin() + at, p.end());
  return p;
}
vector<P> minkowski(vector<P> a, vector<P> b) {
  a = normalize(a);
  b = normalize(b);
  if (a.size() < 3 || b.size() < 3) {
    vector<P> s;
    for (P x : a)
      for (P y : b)
        s.push_back(x + y);
    return hull(s);
  }
  int n = a.size(), m = b.size(), i = 0, j = 0;
  vector<P> r = {a[0] + b[0]};
  while (i < n || j < m) {
    P ea = i < n ? a[(i + 1) % n] - a[i] : P{0, 0};
    P eb = j < m ? b[(j + 1) % m] - b[j] : P{0, 0};
    long long z = (i < n && j < m) ? cross(ea, eb) : 0;
    P step;
    if (j == m || (i < n && z > 0))
      step = ea, ++i;
    else if (i == n || z < 0)
      step = eb, ++j;
    else
      step = ea + eb, ++i, ++j;
    r.push_back(r.back() + step);
  }
  r.pop_back();
  return hull(r);
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
  int n, m, q;
  if (!(cin >> n >> m >> q))
    return 0;
  vector<P> a(n), b(m);
  for (auto &x : a)
    cin >> x.x >> x.y;
  for (auto &x : b)
    cin >> x.x >> x.y;
  reverse(b.begin(), b.end());
  for (auto &x : b)
    x = P{-x.x, -x.y};
  auto s = minkowski(a, b);
  while (q--) {
    P x;
    cin >> x.x >> x.y;
    cout << (locate(s, x) >= 0 ? "YES\n" : "NO\n");
  }
}
