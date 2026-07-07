#include <bits/stdc++.h>
using namespace std;

int days_needed(const vector<long long> &weights, long long capacity) {
    int days = 1;
    long long cur = 0;
    for (long long w : weights) {
        if (cur + w <= capacity) {
            cur += w;
        } else {
            ++days;
            cur = w;
        }
    }
    return days;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, d;
        cin >> n >> d;
        vector<long long> weights(n);
        long long lo = 0;
        long long hi = 0;
        for (long long &w : weights) {
            cin >> w;
            lo = max(lo, w);
            hi += w;
        }
        while (lo < hi) {
            long long mid = lo + (hi - lo) / 2;
            if (days_needed(weights, mid) <= d) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        cout << lo << '\n';
    }

    return 0;
}

