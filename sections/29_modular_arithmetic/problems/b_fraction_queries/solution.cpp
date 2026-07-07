#include <bits/stdc++.h>
using namespace std;

long long mod_pow(long long a, long long b, long long mod) {
    a %= mod;
    long long result = 1 % mod;
    while (b > 0) {
        if (b & 1LL) result = (__int128)result * a % mod;
        a = (__int128)a * a % mod;
        b >>= 1LL;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long p;
    int q;
    if (!(cin >> p >> q)) return 0;
    while (q--) {
        long long a, b;
        cin >> a >> b;
        long long inv = mod_pow(b, p - 2, p);
        long long answer = (__int128)(a % p) * inv % p;
        cout << answer << '\n';
    }
    return 0;
}
