#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  string s;
  cin >> s;
  int n = s.size(), i = 0, j = 1, k = 0;
  while (i < n && j < n && k < n) {
    char a = s[(i + k) % n], b = s[(j + k) % n];
    if (a == b) {
      ++k;
      continue;
    }
    if (a > b) {
      i = i + k + 1;
      if (i == j)
        ++i;
    } else {
      j = j + k + 1;
      if (i == j)
        ++j;
    }
    k = 0;
  }
  int at = min(i, j);
  cout << s.substr(at) + s.substr(0, at) << '\n' << at + 1 << '\n';
}
