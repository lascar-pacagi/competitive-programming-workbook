#include <bits/stdc++.h>
using namespace std;

vector<int> build_spf(int limit) {
    vector<int> spf(limit + 1);
    iota(spf.begin(), spf.end(), 0);
    if (limit >= 1) spf[1] = 1;
    for (long long p = 2; p * p <= limit; ++p) {
        if (spf[p] == p) {
            for (long long multiple = p * p; multiple <= limit; multiple += p) {
                if (spf[multiple] == multiple) spf[multiple] = p;
            }
        }
    }
    return spf;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;
    vector<int> values(q);
    for (int &value : values) cin >> value;
    int limit = *max_element(values.begin(), values.end());
    vector<int> spf = build_spf(limit);

    for (int value : values) {
        int remaining = value;
        long long multiplier = 1;
        while (remaining > 1) {
            int prime = spf[remaining];
            bool odd_exponent = false;
            while (remaining % prime == 0) {
                odd_exponent = !odd_exponent;
                remaining /= prime;
            }
            if (odd_exponent) multiplier *= prime;
        }
        cout << multiplier << '\n';
    }
    return 0;
}
