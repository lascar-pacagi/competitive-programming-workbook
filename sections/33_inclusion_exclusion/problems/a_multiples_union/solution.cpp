#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> d(m);
    for (long long &x : d) cin >> x;

    long long answer = 0;
    for (int mask = 1; mask < (1 << m); mask++) {
        __int128 lcm = 1;
        int bits = 0;
        bool ok = true;
        for (int i = 0; i < m; i++) {
            if (mask & (1 << i)) {
                bits++;
                long long g = gcd((long long)min<__int128>(lcm, LLONG_MAX), d[i]);
                lcm = lcm / g * d[i];
                if (lcm > n) {
                    ok = false;
                    break;
                }
            }
        }
        if (!ok) continue;
        long long count = n / (long long)lcm;
        if (bits % 2) answer += count;
        else answer -= count;
    }
    cout << answer << '\n';
    return 0;
}
