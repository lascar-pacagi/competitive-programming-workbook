#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  if (!(cin >> n))
    return 0;
  priority_queue<long long> left;
  long long answer = 0;
  for (int i = 0; i < n; ++i) {
    long long x;
    cin >> x;
    left.push(x);
    left.push(x);
    answer += left.top() - x;
    left.pop();
  }
  cout << answer << '\n';
}
