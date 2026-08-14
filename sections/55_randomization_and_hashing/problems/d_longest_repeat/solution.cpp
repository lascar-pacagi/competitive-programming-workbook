#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;
    const long long mod1 = 1'000'000'007, mod2 = 1'000'000'009, base = 911'382'323;
    int n = (int)s.size();
    vector<long long> power1(n + 1, 1), power2(n + 1, 1), hash1(n + 1), hash2(n + 1);
    for (int index = 1; index <= n; ++index) {
        power1[index] = power1[index - 1] * base % mod1;
        power2[index] = power2[index - 1] * base % mod2;
        hash1[index] = (hash1[index - 1] * base + s[index - 1]) % mod1;
        hash2[index] = (hash2[index - 1] * base + s[index - 1]) % mod2;
    }
    auto repeated = [&](int length) {
        unordered_set<unsigned long long> seen;
        seen.reserve(2 * (n - length + 1));
        for (int left = 0; left + length <= n; ++left) {
            int right = left + length;
            int first = (hash1[right] - hash1[left] * power1[length] % mod1 + mod1) % mod1;
            int second = (hash2[right] - hash2[left] * power2[length] % mod2 + mod2) % mod2;
            unsigned long long key = (unsigned long long)first * mod2 + second;
            if (!seen.insert(key).second) return true;
        }
        return false;
    };
    int low = 1, high = n, answer = 0;
    while (low <= high) {
        int middle = (low + high) / 2;
        if (repeated(middle)) answer = middle, low = middle + 1;
        else high = middle - 1;
    }
    cout << answer << '\n';
}
