#include <bits/stdc++.h>
#include "../../ntt.hpp"
using namespace std;
using course_ntt::MOD;
using course_ntt::convolution;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    string s, t;
    if (!(cin >> n >> s >> t)) return 0;

    // Equality of two two-bit symbols is
    // (1+xX)(1+yY)/4 = (1+xX+yY+xyXY)/4 for signs +/-1.
    const int inverse_four = course_ntt::power(4, MOD - 2);
    const string alphabet = "ACGT";
    vector<int> score(n, n);
    for (int feature = 0; feature < 3; ++feature) {
        vector<int> left(n), doubled_right(2 * n);
        for (int i = 0; i < n; ++i) {
            int a = alphabet.find(s[i]);
            int b = alphabet.find(t[i]);
            int sign_a = feature == 0 ? (a & 1) : feature == 1 ? (a >> 1) : ((a & 1) ^ (a >> 1));
            int sign_b = feature == 0 ? (b & 1) : feature == 1 ? (b >> 1) : ((b & 1) ^ (b >> 1));
            left[n - 1 - i] = sign_a ? MOD - 1 : 1;
            int value = sign_b ? MOD - 1 : 1;
            doubled_right[i] = doubled_right[i + n] = value;
        }
        vector<int> product = convolution(left, doubled_right);
        for (int shift = 0; shift < n; ++shift) {
            score[shift] += product[n - 1 + shift];
            if (score[shift] >= MOD) score[shift] -= MOD;
        }
    }
    int best = -1, best_shift = 0;
    for (int shift = 0; shift < n; ++shift) {
        int matches = static_cast<int>(1LL * score[shift] * inverse_four % MOD);
        if (matches > best) best = matches, best_shift = shift;
    }
    cout << best << ' ' << best_shift << '\n';
}
