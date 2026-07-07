#include <bits/stdc++.h>
using namespace std;

int groups_needed(const vector<long long> &a, long long limit) {
    int groups = 1;
    long long current = 0;
    for (long long x : a) {
        if (current + x <= limit) {
            current += x;
        } else {
            ++groups;
            current = x;
        }
    }
    return groups;
}

long long solve_case(const vector<long long> &a, int d) {
    long long lo = *max_element(a.begin(), a.end());
    long long hi = accumulate(a.begin(), a.end(), 0LL);
    while (lo < hi) {
        long long mid = lo + (hi - lo) / 2;
        if (groups_needed(a, mid) <= d) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    return lo;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, d;
        cin >> n >> d;
        vector<long long> a(n);
        for (long long &x : a) cin >> x;
        cout << solve_case(a, d) << '\n';
    }

    return 0;
}

