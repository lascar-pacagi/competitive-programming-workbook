#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1'000'000'007LL;

long long mod_pow(long long base, long long exponent) {
    long long result = 1;
    while (exponent > 0) {
        if (exponent & 1LL) result = result * base % MOD;
        base = base * base % MOD;
        exponent >>= 1LL;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;
    vector<pair<int, int>> queries(q);
    int limit = 0;
    for (auto& [red, blue] : queries) {
        cin >> red >> blue;
        limit = max(limit, max(red, blue + 1));
    }

    vector<long long> fact(limit + 1, 1), invfact(limit + 1, 1);
    for (int i = 1; i <= limit; ++i) fact[i] = fact[i - 1] * i % MOD;
    invfact[limit] = mod_pow(fact[limit], MOD - 2);
    for (int i = limit; i >= 1; --i) invfact[i - 1] = invfact[i] * i % MOD;

    for (auto [red, blue] : queries) {
        if (red > blue + 1) {
            cout << 0 << '\n';
            continue;
        }
        long long choose_slots = fact[blue + 1] * invfact[red] % MOD
                               * invfact[blue + 1 - red] % MOD;
        long long answer = choose_slots * fact[red] % MOD * fact[blue] % MOD;
        cout << answer << '\n';
    }
    return 0;
}
