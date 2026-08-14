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
    vector<int> queries(q);
    int maximum = 1;
    for (int& value : queries) {
        cin >> value;
        maximum = max(maximum, value);
    }

    vector<int> divisor_count(maximum + 1);
    vector<int64> expectation_sum(maximum + 1);
    vector<int64> expectation(maximum + 1);

    for (int divisor = 1; divisor <= maximum; ++divisor) {
        if (divisor > 1) {
            expectation[divisor] = (
                1 + expectation_sum[divisor]
                * power(divisor_count[divisor], MOD - 2)
            ) % MOD;
        }
        for (int multiple = 2 * divisor;
             multiple <= maximum;
             multiple += divisor) {
            ++divisor_count[multiple];
            expectation_sum[multiple] += expectation[divisor];
            expectation_sum[multiple] %= MOD;
        }
    }

    for (int value : queries)
        cout << expectation[value] << '\n';
}
