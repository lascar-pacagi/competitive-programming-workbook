#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s, answer;
    int k;
    cin >> s >> k;
    int removals = (int)s.size() - k;
    for (char c : s) {
        while (removals && !answer.empty() && answer.back() > c) {
            answer.pop_back();
            --removals;
        }
        answer.push_back(c);
    }
    answer.resize(k);
    cout << answer << '\n';
}
