#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007LL;

long long mod_pow(long long a, long long b) {
    long long result = 1;
    while (b > 0) {
        if (b & 1LL) result = result * a % MOD;
        a = a * a % MOD;
        b >>= 1LL;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;
    vector<int> values(q);
    int limit = 0;
    for (int &n : values) {
        cin >> n;
        limit = max(limit, n);
    }
    vector<long long> harmonic(limit + 1, 0);
    for (int i = 1; i <= limit; i++) {
        harmonic[i] = (harmonic[i - 1] + mod_pow(i, MOD - 2)) % MOD;
    }
    for (int n : values) cout << n * harmonic[n] % MOD << '\n';
    return 0;
}
