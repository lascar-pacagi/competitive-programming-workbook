#include <bits/stdc++.h>
using namespace std;

vector<long long> solve_case(const vector<long long> &a) {
    vector<long long> ans(a.size(), -1);
    vector<long long> st;
    for (int i = (int)a.size() - 1; i >= 0; --i) {
        while (!st.empty() && st.back() <= a[i]) {
            st.pop_back();
        }
        if (!st.empty()) {
            ans[i] = st.back();
        }
        st.push_back(a[i]);
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
        vector<long long> ans = solve_case(a);
        for (int i = 0; i < n; ++i) {
            if (i) cout << ' ';
            cout << ans[i];
        }
        cout << '\n';
    }

    return 0;
}

