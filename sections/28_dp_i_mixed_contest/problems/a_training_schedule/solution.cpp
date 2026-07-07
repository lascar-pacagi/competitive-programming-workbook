#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    const int INF = 1e9;
    array<int, 3> dp = {0, INF, INF};
    for (int day = 0; day < n; day++) {
        int available;
        cin >> available;
        array<int, 3> ndp = {min({dp[0], dp[1], dp[2]}) + 1, INF, INF};
        if (available & 1) ndp[1] = min(dp[0], dp[2]);
        if (available & 2) ndp[2] = min(dp[0], dp[1]);
        dp = ndp;
    }
    cout << min({dp[0], dp[1], dp[2]}) << '\n';
    return 0;
}
