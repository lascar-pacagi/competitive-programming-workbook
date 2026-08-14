#include <bits/stdc++.h>
using namespace std;

long long extended_gcd(long long a, long long b, long long& x, long long& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long g = extended_gcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        long long a, b, m;
        cin >> a >> b >> m;

        long long coefficient, unused;
        long long g = extended_gcd(a, m, coefficient, unused);
        if (b % g != 0) {
            cout << -1 << '\n';
            continue;
        }

        long long reduced_modulus = m / g;
        long long scale = b / g;
        long long answer = (coefficient * scale) % reduced_modulus;
        if (answer < 0) answer += reduced_modulus;
        cout << answer << '\n';
    }
    return 0;
}
