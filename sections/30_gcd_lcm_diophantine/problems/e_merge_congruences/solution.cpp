#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
using int128 = __int128_t;

tuple<int64, int64, int64> extended_gcd(int64 a, int64 b) {
    if (b == 0) return {a, 1, 0};
    auto [g, x1, y1] = extended_gcd(b, a % b);
    return {g, y1, x1 - (a / b) * y1};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    cin >> q;
    while (q--) {
        int64 r1, m1, r2, m2;
        cin >> r1 >> m1 >> r2 >> m2;
        auto [g, coefficient, unused] = extended_gcd(m1, m2);
        int64 difference = r2 - r1;
        if (difference % g != 0) {
            cout << -1 << '\n';
            continue;
        }

        int64 reduced_period = m2 / g;
        int64 k = (int128)coefficient * (difference / g) % reduced_period;
        if (k < 0) k += reduced_period;

        int64 period = (m1 / g) * m2;
        int64 answer = (r1 + (int128)m1 * k) % period;
        cout << answer << '\n';
    }
}
