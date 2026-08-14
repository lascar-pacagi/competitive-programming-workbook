#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1'000'000'007;

long long mod_pow(long long base, long long exponent) {
    long long result = 1;

    while (exponent > 0) {
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

    int n;
    cin >> n;

    long long probability_sum = 0;
    long long answer = 0;

    while (n--) {
        long long numerator, denominator;
        cin >> numerator >> denominator;

        long long probability = (
            numerator * mod_pow(denominator, MOD - 2) % MOD
        );

        answer = (
            answer + probability * probability_sum
        ) % MOD;

        probability_sum = (
            probability_sum + probability
        ) % MOD;
    }

    cout << answer << '\n';
}
