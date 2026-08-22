#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
constexpr int64 MOD = 998244353;

vector<int64> combine(
    const vector<int64> &left,
    const vector<int64> &right,
    const vector<int64> &coefficient
) {
    int order = coefficient.size();
    vector<int64> product(2 * order - 1);
    for (int i = 0; i < order; ++i)
        for (int j = 0; j < order; ++j)
            product[i + j] = (product[i + j] + left[i] * right[j]) % MOD;
    for (int degree = 2 * order - 2; degree >= order; --degree)
        for (int back = 1; back <= order; ++back)
            product[degree - back] = (
                product[degree - back] + product[degree] * coefficient[back - 1]
            ) % MOD;
    product.resize(order);
    return product;
}

int64 nth_term(
    const vector<int64> &initial,
    const vector<int64> &coefficient,
    unsigned long long index
) {
    int order = initial.size();
    if (index < static_cast<unsigned long long>(order)) return initial[index];
    vector<int64> result(order), base(order);
    result[0] = 1;
    if (order == 1)
        base[0] = coefficient[0];
    else
        base[1] = 1;
    while (index > 0) {
        if (index & 1) result = combine(result, base, coefficient);
        base = combine(base, base, coefficient);
        index >>= 1;
    }
    int64 answer = 0;
    for (int i = 0; i < order; ++i)
        answer = (answer + result[i] * initial[i]) % MOD;
    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int order;
    unsigned long long index;
    if (!(cin >> order >> index)) return 0;
    vector<int64> initial(order), coefficient(order);
    for (int64 &value : initial) cin >> value;
    for (int64 &value : coefficient) cin >> value;
    cout << nth_term(initial, coefficient, index) << '\n';
}
