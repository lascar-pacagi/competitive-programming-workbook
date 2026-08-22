#include <bits/stdc++.h>
using namespace std;
vector<int> suffix_array(const string &s) {
  int n = s.size();
  vector<int> sa(n), r(n), nr(n);
  iota(sa.begin(), sa.end(), 0);
  for (int i = 0; i < n; ++i)
    r[i] = (unsigned char)s[i];
  for (int k = 1;; k *= 2) {
    sort(sa.begin(), sa.end(), [&](int a, int b) {
      return pair{r[a], a + k < n ? r[a + k] : -1} <
             pair{r[b], b + k < n ? r[b + k] : -1};
    });
    nr[sa[0]] = 0;
    for (int i = 1; i < n; ++i) {
      int a = sa[i - 1], b = sa[i];
      nr[b] = nr[a] + (pair{r[a], a + k < n ? r[a + k] : -1} <
                       pair{r[b], b + k < n ? r[b + k] : -1});
    }
    r = nr;
    if (r[sa.back()] == n - 1)
      break;
  }
  return sa;
}
vector<int> lcp_array(const string &s, const vector<int> &sa) {
  int n = s.size(), h = 0;
  vector<int> rank(n), lcp(max(0, n - 1));
  for (int i = 0; i < n; ++i)
    rank[sa[i]] = i;
  for (int i = 0; i < n; ++i) {
    int q = rank[i];
    if (!q)
      continue;
    int j = sa[q - 1];
    while (i + h < n && j + h < n && s[i + h] == s[j + h])
      ++h;
    lcp[q - 1] = h;
    if (h)
      --h;
  }
  return lcp;
}

struct DSU {
  vector<int> p, z;
  DSU(int n) : p(n), z(n, 1) { iota(p.begin(), p.end(), 0); }
  int f(int x) { return p[x] == x ? x : p[x] = f(p[x]); }
  int unite(int a, int b) {
    a = f(a);
    b = f(b);
    if (a == b)
      return z[a];
    if (z[a] < z[b])
      swap(a, b);
    p[b] = a;
    return z[a] += z[b];
  }
};
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  string s;
  cin >> s;
  int n = s.size();
  auto sa = suffix_array(s), lcp = lcp_array(s, sa);
  vector<array<int, 3>> e;
  for (int i = 0; i < n - 1; ++i)
    e.push_back({lcp[i], i, i + 1});
  sort(e.rbegin(), e.rend());
  DSU d(n);
  vector<int> ans(n + 1);
  ans[1] = n;
  for (auto [w, a, b] : e) {
    int size = d.unite(a, b);
    ans[size] = max(ans[size], w);
  }
  for (int k = n - 1; k; --k)
    ans[k] = max(ans[k], ans[k + 1]);
  for (int k = 1; k <= n; ++k)
    cout << ans[k] << " \n"[k == n];
}
