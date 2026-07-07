#include <bits/stdc++.h>
using namespace std;

string complete(string s) {
    int n = (int)s.size();
    if (n % 2) return "IMPOSSIBLE";

    int need_open = n / 2;
    int need_close = n / 2;
    for (char ch : s) {
        if (ch == '(') --need_open;
        if (ch == ')') --need_close;
    }
    if (need_open < 0 || need_close < 0) return "IMPOSSIBLE";

    for (char &ch : s) {
        if (ch == '?') {
            if (need_open > 0) {
                ch = '(';
                --need_open;
            } else {
                ch = ')';
                --need_close;
            }
        }
    }

    int balance = 0;
    for (int i = 0; i < n; ++i) {
        balance += (s[i] == '(' ? 1 : -1);
        if (balance < 0) return "IMPOSSIBLE";
        if (i + 1 < n && balance == 0) return "IMPOSSIBLE";
    }
    if (balance != 0) return "IMPOSSIBLE";
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        string s;
        cin >> s;
        cout << complete(s) << '\n';
    }

    return 0;
}

