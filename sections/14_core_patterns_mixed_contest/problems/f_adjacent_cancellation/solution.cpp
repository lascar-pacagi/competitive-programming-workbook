#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int tests;
    cin >> tests;
    while (tests--) {
        string s, stack;
        cin >> s;
        for (char c : s) {
            if (!stack.empty() && stack.back() == c) stack.pop_back();
            else stack.push_back(c);
        }
        cout << (stack.empty() ? "EMPTY" : stack) << '\n';
    }
}
