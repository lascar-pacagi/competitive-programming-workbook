#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<long long> bit;

    explicit Fenwick(int size) : n(size), bit(size + 1, 0) {}

    void add(int index, long long delta) {
        for (; index <= n; index += index & -index) bit[index] += delta;
    }

    long long sum(int index) const {
        long long result = 0;
        for (; index > 0; index -= index & -index) result += bit[index];
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    Fenwick coefficients(n + 1), weighted_coefficients(n + 1);

    auto add_range = [&](int left, int right, long long delta) {
        coefficients.add(left, delta);
        coefficients.add(right + 1, -delta);
        weighted_coefficients.add(left, delta * left);
        weighted_coefficients.add(right + 1, -delta * (right + 1));
    };
    auto prefix_sum = [&](int position) {
        long long coefficient_sum = coefficients.sum(position);
        long long weighted_sum = weighted_coefficients.sum(position);
        return (position + 1LL) * coefficient_sum - weighted_sum;
    };

    while (q--) {
        int type, left, right;
        cin >> type >> left >> right;
        if (type == 1) {
            long long delta;
            cin >> delta;
            add_range(left, right, delta);
        } else {
            cout << prefix_sum(right) - prefix_sum(left - 1) << '\n';
        }
    }
    return 0;
}
