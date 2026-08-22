#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll extended_gcd(ll a, ll b, ll& x, ll& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }

    ll x1, y1;
    ll g = extended_gcd(b, a % b, x1, y1);
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
        ll a, b, c, m;
        cin >> a >> b >> c >> m;

        ll target = (b - c) % m;
        if (target < 0)
            target += m;

        ll x, y;
        ll g = extended_gcd(a, m, x, y);
        if (target % g != 0) {
            cout << -1 << '\n';
            continue;
        }

        ll reduced_modulus = m / g;
        __int128 value = (__int128)(target / g) * x;
        ll answer = (ll)(value % reduced_modulus);
        if (answer < 0)
            answer += reduced_modulus;
        cout << answer << '\n';
    }
}
