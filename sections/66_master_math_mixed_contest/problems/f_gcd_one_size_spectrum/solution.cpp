#include <bits/stdc++.h>
#include "../../../65_polynomial_algorithms_recurrences/ntt.hpp"
using namespace std;
using course_ntt::MOD;
using course_ntt::convolution;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n);
    int maximum = 1;
    for (int &value : values) cin >> value, maximum = max(maximum, value);

    vector<int> frequency(maximum + 1);
    for (int value : values) ++frequency[value];
    vector<int> divisible(maximum + 1);
    for (int d = 1; d <= maximum; ++d)
        for (int multiple = d; multiple <= maximum; multiple += d)
            divisible[d] += frequency[multiple];

    vector<int> mu(maximum + 1), primes;
    vector<bool> composite(maximum + 1);
    mu[1] = 1;
    for (int value = 2; value <= maximum; ++value) {
        if (!composite[value]) primes.push_back(value), mu[value] = -1;
        for (int prime : primes) {
            if (1LL * value * prime > maximum) break;
            composite[value * prime] = true;
            if (value % prime == 0) {
                mu[value * prime] = 0;
                break;
            }
            mu[value * prime] = -mu[value];
        }
    }

    vector<int> bucket(n + 1);
    for (int d = 1; d <= maximum; ++d) {
        bucket[divisible[d]] += mu[d];
        if (bucket[divisible[d]] < 0) bucket[divisible[d]] += MOD;
        if (bucket[divisible[d]] >= MOD) bucket[divisible[d]] -= MOD;
    }

    vector<int> factorial(n + 1, 1), inverse_factorial(n + 1, 1);
    for (int i = 1; i <= n; ++i)
        factorial[i] = static_cast<int>(1LL * factorial[i - 1] * i % MOD);
    inverse_factorial[n] = course_ntt::power(factorial[n], MOD - 2);
    for (int i = n; i >= 1; --i)
        inverse_factorial[i - 1] = static_cast<int>(1LL * inverse_factorial[i] * i % MOD);

    vector<int> reversed(n + 1), inverse(n + 1);
    for (int count = 0; count <= n; ++count) {
        reversed[n - count] = static_cast<int>(1LL * bucket[count] * factorial[count] % MOD);
        inverse[count] = inverse_factorial[count];
    }
    vector<int> product = convolution(reversed, inverse);
    for (int size = 1; size <= n; ++size) {
        int answer = static_cast<int>(1LL * product[n - size] * inverse_factorial[size] % MOD);
        cout << answer << (size == n ? '\n' : ' ');
    }
}
