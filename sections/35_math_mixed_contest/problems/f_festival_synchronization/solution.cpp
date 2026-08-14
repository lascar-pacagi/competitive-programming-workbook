#include <bits/stdc++.h>
using namespace std;

using int64 = long long;

int64 extended_gcd(int64 a, int64 b, int64& x, int64& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    int64 x1, y1;
    int64 g = extended_gcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    cin >> q;
    while (q--) {
        int64 r1, m1, r2, m2;
        cin >> r1 >> m1 >> r2 >> m2;

        int64 inverse, unused;
        int64 g = extended_gcd(m1, m2, inverse, unused);
        int64 difference = r2 - r1;
        if (difference % g != 0) {
            cout << -1 << '\n';
            continue;
        }

        int64 reduced_modulus = m2 / g;
        int64 multiplier = static_cast<int64>(
            (__int128)(difference / g) * inverse % reduced_modulus
        );
        if (multiplier < 0)
            multiplier += reduced_modulus;

        int64 period = m1 / g * m2;
        int64 answer = static_cast<int64>(
            ((__int128)m1 * multiplier + r1) % period
        );
        cout << answer << '\n';
    }
}
