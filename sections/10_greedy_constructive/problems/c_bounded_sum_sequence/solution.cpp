#include <bits/stdc++.h>
using namespace std;

string construct(long long n, long long m, long long s) {
    if (s < n || s > n * m) return "IMPOSSIBLE";

    vector<long long> ans;
    ans.reserve((size_t)n);
    long long remaining = s;
    for (long long pos = 0; pos < n; ++pos) {
        long long left = n - pos - 1;
        long long x = max(1LL, remaining - left * m);
        ans.push_back(x);
        remaining -= x;
    }

    stringstream ss;
    for (int i = 0; i < (int)ans.size(); ++i) {
        if (i) ss << ' ';
        ss << ans[i];
    }
    return ss.str();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        long long n, m, s;
        cin >> n >> m >> s;
        cout << construct(n, m, s) << '\n';
    }

    return 0;
}

