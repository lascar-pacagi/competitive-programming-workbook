#include <bits/stdc++.h>
using namespace std;

int solve_case(const vector<int> &a, int m) {
    vector<int> freq(m + 1, 0);
    int have = 0;
    int best = (int)a.size() + 1;
    int left = 0;
    for (int right = 0; right < (int)a.size(); ++right) {
        int value = a[right];
        if (1 <= value && value <= m) {
            if (freq[value] == 0) ++have;
            ++freq[value];
        }
        while (have == m) {
            best = min(best, right - left + 1);
            int old = a[left];
            if (1 <= old && old <= m) {
                --freq[old];
                if (freq[old] == 0) --have;
            }
            ++left;
        }
    }
    return best == (int)a.size() + 1 ? -1 : best;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n >> m;
        vector<int> a(n);
        for (int &x : a) cin >> x;
        cout << solve_case(a, m) << '\n';
    }

    return 0;
}

