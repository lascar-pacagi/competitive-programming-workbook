#include <bits/stdc++.h>
using namespace std;
bool ok(vector<vector<int>> &a, int x) {
  int n = a.size();
  vector<int> match(n, -1);
  function<bool(int, vector<char> &)> dfs = [&](int u, vector<char> &seen) {
    for (int v = 0; v < n; v++)
      if (a[u][v] <= x && !seen[v]) {
        seen[v] = 1;
        if (match[v] < 0 || dfs(match[v], seen)) {
          match[v] = u;
          return true;
        }
      }
    return false;
  };
  for (int u = 0; u < n; u++) {
    vector<char> seen(n);
    if (!dfs(u, seen))
      return false;
  }
  return true;
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<vector<int>> a(n, vector<int>(n));
  vector<int> v;
  for (auto &r : a)
    for (int &x : r)
      cin >> x, v.push_back(x);
  sort(v.begin(), v.end());
  v.erase(unique(v.begin(), v.end()), v.end());
  int l = -1, r = v.size() - 1;
  while (r - l > 1) {
    int m = (l + r) / 2;
    (ok(a, v[m]) ? r : l) = m;
  }
  cout << v[r] << '\n';
}