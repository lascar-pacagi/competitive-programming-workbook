#include <bits/stdc++.h>
#include "../../ntt.hpp"
using namespace std;
using course_ntt::convolution;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, target;
    if (!(cin >> n >> target)) return 0;

    struct Compare {
        bool operator()(const vector<int> &a, const vector<int> &b) const {
            return a.size() > b.size();
        }
    };
    priority_queue<vector<int>, vector<vector<int>>, Compare> products;
    for (int i = 0, bound; i < n; ++i) {
        cin >> bound;
        if (bound > 0) products.push(vector<int>(min(bound, target) + 1, 1));
    }
    if (products.empty()) {
        cout << (target == 0) << '\n';
        return 0;
    }
    while (products.size() > 1) {
        auto left = products.top(); products.pop();
        auto right = products.top(); products.pop();
        products.push(convolution(left, right, target + 1));
    }
    const auto &answer = products.top();
    cout << (target < static_cast<int>(answer.size()) ? answer[target] : 0) << '\n';
}
