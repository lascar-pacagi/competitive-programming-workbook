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

int64 choose_small_k(int64 top, int k, int64 inverse_factorial) {
    if (top < k || top < 0)
        return 0;
    int64 numerator = 1;
    for (int i = 1; i <= k; ++i) {
        numerator = numerator * ((top - i + 1) % MOD) % MOD;
    }
    return numerator * inverse_factorial % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    int64 target;
    cin >> n >> target;
    vector<int64> cap(n);
    for (int64& value : cap)
        cin >> value;

    int subset_count = 1 << n;
    int64 factorial = 1;
    for (int i = 1; i < n; ++i)
        factorial = factorial * i % MOD;
    int64 inverse_factorial = power(factorial, MOD - 2);
    vector<int64> shifted_sum(subset_count);
    int64 answer = 0;
    for (int mask = 0; mask < subset_count; ++mask) {
        if (mask) {
            int bit = __builtin_ctz(mask);
            shifted_sum[mask] = shifted_sum[mask ^ (1 << bit)] + cap[bit] + 1;
        }
        int64 remaining = target - shifted_sum[mask];
        int64 ways = choose_small_k(
            remaining + n - 1, n - 1, inverse_factorial
        );
        if (__builtin_popcount(static_cast<unsigned>(mask)) & 1)
            answer = (answer - ways + MOD) % MOD;
        else
            answer = (answer + ways) % MOD;
    }

    cout << answer << '\n';
}
