#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s, answer;
    int k;
    cin >> s >> k;
    for (char c : s) {
        while (k > 0 && !answer.empty() && answer.back() > c) {
            answer.pop_back();
            --k;
        }
        answer.push_back(c);
    }
    answer.resize(answer.size() - k);
    cout << answer << '\n';
}
