#include <bits/stdc++.h>
#include "../../../65_polynomial_algorithms_recurrences/ntt.hpp"
using namespace std;
using course_ntt::convolution;

vector<int> correlation(const vector<int> &left, const vector<int> &right) {
    int n = left.size();
    vector<int> reversed(n), doubled(2 * n);
    for (int i = 0; i < n; ++i) {
        reversed[n - 1 - i] = left[i];
        doubled[i] = doubled[i + n] = right[i];
    }
    vector<int> product = convolution(reversed, doubled);
    vector<int> result(n);
    for (int shift = 0; shift < n; ++shift)
        result[shift] = product[n - 1 + shift];
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    string s, t;
    if (!(cin >> n >> s >> t)) return 0;
    vector<int> concrete_s(n), concrete_t(n);
    for (int i = 0; i < n; ++i) {
        concrete_s[i] = s[i] != '?';
        concrete_t[i] = t[i] != '?';
    }
    vector<int> both = correlation(concrete_s, concrete_t), matches(n);
    for (char letter : string("ACGT")) {
        vector<int> in_s(n), in_t(n);
        for (int i = 0; i < n; ++i) {
            in_s[i] = s[i] == letter;
            in_t[i] = t[i] == letter;
        }
        vector<int> same = correlation(in_s, in_t);
        for (int shift = 0; shift < n; ++shift) matches[shift] += same[shift];
    }
    int count = 0, first = -1;
    for (int shift = 0; shift < n; ++shift)
        if (both[shift] == matches[shift]) {
            if (first == -1) first = shift;
            ++count;
        }
    cout << count << ' ' << first << '\n';
}
