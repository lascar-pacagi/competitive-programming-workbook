#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
const int64 MOD = 1'000'000'007;

int64 power(int64 base, int64 exponent) {
    int64 result = 1;
    while (exponent) {
        if (exponent & 1)
            result = result * base % MOD;
        base = base * base % MOD;
        exponent >>= 1;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    cin >> q;
    vector<tuple<int64, int, int>> queries(q);
    int maximum_m = 0;
    for (auto& [n, m, k] : queries) {
        cin >> n >> m >> k;
        maximum_m = max(maximum_m, m);
    }

    vector<int64> factorial(maximum_m + 1, 1);
    vector<int64> inverse_factorial(maximum_m + 1, 1);
    for (int i = 1; i <= maximum_m; ++i)
        factorial[i] = factorial[i - 1] * i % MOD;
    inverse_factorial[maximum_m] = power(factorial[maximum_m], MOD - 2);
    for (int i = maximum_m; i >= 1; --i)
        inverse_factorial[i - 1] = inverse_factorial[i] * i % MOD;

    auto choose = [&](int n, int k) {
        return factorial[n] * inverse_factorial[k] % MOD
            * inverse_factorial[n - k] % MOD;
    };

    for (auto [length, colors, used] : queries) {
        int64 onto = 0;
        for (int missing = 0; missing <= used; ++missing) {
            int64 term = choose(used, missing)
                * power(used - missing, length) % MOD;
            if (missing & 1)
                onto = (onto - term + MOD) % MOD;
            else
                onto = (onto + term) % MOD;
        }
        cout << choose(colors, used) * onto % MOD << '\n';
    }
}
