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

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        long long a, b, mod;
        cin >> a >> b >> mod;
        cout << mod_pow(a, b, mod) << '\n';
    }
    return 0;
}
