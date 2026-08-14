#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  if (!(cin >> n))
    return 0;
  priority_queue<long long, vector<long long>, greater<long long>> ends;
  int answer = 0;
  for (int i = 0; i < n; i++) {
    long long s, e;
    cin >> s >> e;
    while (!ends.empty() && ends.top() <= s)
      ends.pop();
    ends.push(e);
    answer = max(answer, (int)ends.size());
    if (i)
      cout << ' ';
    cout << answer;
  }
  cout << '\n';
}
