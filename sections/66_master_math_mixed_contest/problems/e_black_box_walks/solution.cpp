#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
constexpr int64 MOD = 998244353;

int64 power(int64 base, int64 exponent) {
    int64 result = 1;
    while (exponent) {
        if (exponent & 1) result = result * base % MOD;
        base = base * base % MOD;
        exponent >>= 1;
    }
    return result;
}

vector<int64> berlekamp_massey(const vector<int64> &sequence) {
    vector<int64> current{1}, saved{1};
    int length = 0, shift = 1;
    int64 saved_discrepancy = 1;
    for (int position = 0; position < static_cast<int>(sequence.size()); ++position) {
        int64 discrepancy = sequence[position];
        for (int i = 1; i <= length; ++i)
            discrepancy = (discrepancy + current[i] * sequence[position - i]) % MOD;
        if (discrepancy == 0) {
            ++shift;
            continue;
        }
        vector<int64> previous = current;
        int64 scale = discrepancy * power(saved_discrepancy, MOD - 2) % MOD;
        if (current.size() < saved.size() + shift)
            current.resize(saved.size() + shift);
        for (int i = 0; i < static_cast<int>(saved.size()); ++i) {
            current[i + shift] = (current[i + shift] - scale * saved[i]) % MOD;
            if (current[i + shift] < 0) current[i + shift] += MOD;
        }
        if (2 * length <= position) {
            length = position + 1 - length;
            saved = move(previous);
            saved_discrepancy = discrepancy;
            shift = 1;
        } else {
            ++shift;
        }
    }
    vector<int64> recurrence(length);
    for (int i = 0; i < length; ++i)
        recurrence[i] = (MOD - current[i + 1]) % MOD;
    return recurrence;
}

vector<int64> combine(const vector<int64> &a, const vector<int64> &b,
                      const vector<int64> &recurrence) {
    int order = recurrence.size();
    vector<int64> product(2 * order - 1);
    for (int i = 0; i < order; ++i)
        for (int j = 0; j < order; ++j)
            product[i + j] = (product[i + j] + a[i] * b[j]) % MOD;
    for (int degree = 2 * order - 2; degree >= order; --degree)
        for (int back = 1; back <= order; ++back)
            product[degree - back] = (
                product[degree - back] + product[degree] * recurrence[back - 1]
            ) % MOD;
    product.resize(order);
    return product;
}

int64 nth_term(const vector<int64> &sequence, const vector<int64> &recurrence,
               unsigned long long index) {
    if (index < sequence.size()) return sequence[index];
    int order = recurrence.size();
    if (order == 0) return 0;
    vector<int64> result(order), base(order);
    result[0] = 1;
    if (order == 1) base[0] = recurrence[0];
    else base[1] = 1;
    while (index) {
        if (index & 1) result = combine(result, base, recurrence);
        base = combine(base, base, recurrence);
        index >>= 1;
    }
    int64 answer = 0;
    for (int i = 0; i < order; ++i)
        answer = (answer + result[i] * sequence[i]) % MOD;
    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, start, target;
    unsigned long long length;
    if (!(cin >> n >> m >> length >> start >> target)) return 0;
    --start; --target;
    struct Edge { int from, to; int64 weight; };
    vector<Edge> edges(m);
    for (auto &[from, to, weight] : edges) {
        cin >> from >> to >> weight;
        --from; --to;
    }

    vector<int64> state(n), sequence(2 * n + 1);
    state[start] = 1;
    for (int step = 0; step <= 2 * n; ++step) {
        sequence[step] = state[target];
        vector<int64> next(n);
        for (auto [from, to, weight] : edges)
            next[to] = (next[to] + state[from] * weight) % MOD;
        state.swap(next);
    }
    vector<int64> recurrence = berlekamp_massey(sequence);
    cout << nth_term(sequence, recurrence, length) << '\n';
}
