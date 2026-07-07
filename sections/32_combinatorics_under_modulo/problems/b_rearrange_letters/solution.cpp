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

    string s;
    if (!(cin >> s)) return 0;
    int n = (int)s.size();
    vector<long long> fact(n + 1, 1);
    for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % MOD;
    vector<int> cnt(26, 0);
    for (char ch : s) cnt[ch - 'a']++;
    long long answer = fact[n];
    for (int c : cnt) answer = answer * mod_pow(fact[c], MOD - 2) % MOD;
    cout << answer << '\n';
    return 0;
}
