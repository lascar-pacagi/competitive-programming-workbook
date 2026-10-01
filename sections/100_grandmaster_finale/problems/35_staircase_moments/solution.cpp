#include <bits/stdc++.h>
using namespace std;

// F, G, H = sums over x = 0..n of q, x q, q^2 with q = floor((a x + b) / c).
// Reduce a, b below c (pulling out the linear parts), then exchange the roles
// of x and q: the lattice points under the line are counted by rows instead
// of columns, which turns (a, c) into (c, a) exactly like Euclid's algorithm.

typedef long long ll;
const ll MOD = 998244353, INV2 = (MOD + 1) / 2;
ll INV6;

struct Triple {
    ll f, g, h;
};

ll power(ll b, ll e) {
    ll r = 1;
    for (b %= MOD; e; e >>= 1, b = b * b % MOD)
        if (e & 1) r = r * b % MOD;
    return r;
}

Triple solve(ll a, ll b, ll c, ll n) {
    ll nm = n % MOD;
    ll s1 = nm * ((nm + 1) % MOD) % MOD * INV2 % MOD;
    ll s2 = nm * ((nm + 1) % MOD) % MOD * ((2 * nm + 1) % MOD) % MOD * INV6 % MOD;
    if (a == 0) {
        ll q = b / c % MOD, n1 = (nm + 1) % MOD;
        return {n1 * q % MOD, q * s1 % MOD, n1 * q % MOD * q % MOD};
    }
    if (a >= c || b >= c) {
        ll A = a / c % MOD, B = b / c % MOD;
        Triple t = solve(a % c, b % c, c, n);
        ll n1 = (nm + 1) % MOD;
        Triple r;
        r.f = (t.f + A * s1 + B * n1) % MOD;
        r.g = (t.g + A * s2 + B * s1) % MOD;
        r.h = (t.h + A * A % MOD * s2 + B * B % MOD * n1 + 2 * A % MOD * B % MOD * s1 + 2 * B * t.f + 2 * A * t.g) % MOD;
        return r;
    }
    ll m = (ll)(((__int128)a * n + b) / c);
    if (m == 0) return {0, 0, 0};
    Triple t = solve(c, c - b - 1, a, m - 1);
    ll mm = m % MOD;
    Triple r;
    r.f = ((nm * mm - t.f) % MOD + MOD) % MOD;
    r.g = ((mm * nm % MOD * ((nm + 1) % MOD) - t.h - t.f) % MOD + 2 * MOD) % MOD * INV2 % MOD;
    r.h = ((nm * mm % MOD * ((mm + 1) % MOD) - 2 * t.g - 2 * t.f - r.f) % MOD + 5 * MOD) % MOD;
    return r;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    INV6 = power(6, MOD - 2);
    int t;
    cin >> t;
    string out;
    while (t--) {
        ll n, a, b, c;
        cin >> n >> a >> b >> c;
        Triple r = solve(a, b, c, n);
        out += to_string(r.f) + ' ' + to_string(r.g) + ' ' + to_string(r.h) + '\n';
    }
    cout << out;
}
