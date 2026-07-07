#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    long long prev2 = 0, prev1 = 0;
    for (int i = 0; i < n; i++) {
        long long x;
        cin >> x;
        long long cur = max(prev1, prev2 + x);
        prev2 = prev1;
        prev1 = cur;
    }
    cout << prev1 << '\n';
    return 0;
}

