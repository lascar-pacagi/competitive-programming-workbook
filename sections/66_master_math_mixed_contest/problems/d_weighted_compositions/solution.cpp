#include <bits/stdc++.h>
#include "../../../65_polynomial_algorithms_recurrences/ntt.hpp"
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
    priority_queue<vector<int>, vector<vector<int>>, Compare> heap;
    for (int i = 0, weight, cap; i < n; ++i) {
        cin >> weight >> cap;
        int maximum = static_cast<int>(min(1LL * target, 1LL * weight * cap));
        vector<int> polynomial(maximum + 1);
        for (int value = 0; value <= maximum; value += weight) polynomial[value] = 1;
        if (polynomial.size() > 1) heap.push(move(polynomial));
    }
    if (heap.empty()) {
        cout << (target == 0) << '\n';
        return 0;
    }
    while (heap.size() > 1) {
        auto a = heap.top(); heap.pop();
        auto b = heap.top(); heap.pop();
        heap.push(convolution(a, b, target + 1));
    }
    const auto &answer = heap.top();
    cout << (target < static_cast<int>(answer.size()) ? answer[target] : 0) << '\n';
}
