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

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  string s;
  cin >> s;
  auto sa = suffix_array(s), lcp = lcp_array(s, sa);
  for (int i = 0; i < (int)sa.size(); ++i)
    cout << sa[i] + 1 << " \n"[i + 1 == (int)sa.size()];
  for (int i = 0; i < (int)lcp.size(); ++i)
    cout << lcp[i] << " \n"[i + 1 == (int)lcp.size()];
  if (lcp.empty())
    cout << '\n';
}
