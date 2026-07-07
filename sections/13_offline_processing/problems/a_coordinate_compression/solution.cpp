#include <bits/stdc++.h>
using namespace std;

vector<int> solve_case(const vector<long long> &a) {
    vector<long long> values = a;
    sort(values.begin(), values.end());
    values.erase(unique(values.begin(), values.end()), values.end());

    vector<int> ans;
    ans.reserve(a.size());
    for (long long x : a) {
        ans.push_back((int)(lower_bound(values.begin(), values.end(), x) - values.begin()));
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        vector<long long> a(n);
        for (long long &x : a) cin >> x;
        vector<int> ans = solve_case(a);
        for (int i = 0; i < n; ++i) {
            if (i) cout << ' ';
            cout << ans[i];
        }
        cout << '\n';
    }

    return 0;
}

