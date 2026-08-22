#include <bits/stdc++.h>
using namespace std;

struct Query {
    int n, k, index;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    cin >> q;
    vector<Query> queries(q);
    int maximum = 1;
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].n >> queries[i].k;
        queries[i].index = i;
        maximum = max(maximum, queries[i].n);
    }

    vector<int> divisor_count(maximum + 1);
    for (int divisor = 1; divisor <= maximum; ++divisor)
        for (int multiple = divisor; multiple <= maximum; multiple += divisor)
            ++divisor_count[multiple];

    vector<int> order(q);
    iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(), [&](int i, int j) {
        return queries[i].n < queries[j].n;
    });

    vector<long long> seen(101), answer(q);
    int pointer = 0;
    for (int value = 1; value <= maximum; ++value) {
        if (divisor_count[value] <= 100)
            ++seen[divisor_count[value]];
        while (pointer < q && queries[order[pointer]].n == value) {
            const Query& query = queries[order[pointer]];
            answer[query.index] = seen[query.k];
            ++pointer;
        }
    }

    for (long long value : answer)
        cout << value << '\n';
}
