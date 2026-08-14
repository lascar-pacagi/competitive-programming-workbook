#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    vector<int> bit;
    explicit Fenwick(int n) : bit(n + 1, 0) {}

    void add(int index, int delta) {
        for (int n = (int)bit.size(); index < n; index += index & -index) {
            bit[index] += delta;
        }
    }

    int sum(int index) const {
        int result = 0;
        for (; index > 0; index -= index & -index) result += bit[index];
        return result;
    }
};

struct Interval {
    long long left, right;
    int index;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<Interval> ranges(n);
    vector<long long> rights;
    for (int i = 0; i < n; i++) {
        cin >> ranges[i].left >> ranges[i].right;
        ranges[i].index = i;
        rights.push_back(ranges[i].right);
    }
    sort(rights.begin(), rights.end());
    rights.erase(unique(rights.begin(), rights.end()), rights.end());
    sort(ranges.begin(), ranges.end(), [](const Interval& a, const Interval& b) {
        if (a.left != b.left) return a.left < b.left;
        return a.right > b.right;
    });
    auto rank_of = [&](long long right) {
        return int(lower_bound(rights.begin(), rights.end(), right) - rights.begin()) + 1;
    };

    vector<int> contains(n), contained_by(n);
    Fenwick bit((int)rights.size());
    int processed = 0;
    for (int start = 0; start < n;) {
        int end = start + 1;
        while (end < n && ranges[end].left == ranges[start].left &&
               ranges[end].right == ranges[start].right) {
            end++;
        }
        int size = end - start;
        int rank = rank_of(ranges[start].right);
        int base = processed - bit.sum(rank - 1);
        for (int i = start; i < end; i++) contained_by[ranges[i].index] = base + size - 1;
        bit.add(rank, size);
        processed += size;
        start = end;
    }

    bit = Fenwick((int)rights.size());
    for (int end = n; end > 0;) {
        int start = end - 1;
        while (start > 0 && ranges[start - 1].left == ranges[end - 1].left &&
               ranges[start - 1].right == ranges[end - 1].right) {
            start--;
        }
        int size = end - start;
        int rank = rank_of(ranges[start].right);
        int base = bit.sum(rank);
        for (int i = start; i < end; i++) contains[ranges[i].index] = base + size - 1;
        bit.add(rank, size);
        end = start;
    }

    for (int i = 0; i < n; i++) cout << contains[i] << (i + 1 == n ? '\n' : ' ');
    for (int i = 0; i < n; i++) cout << contained_by[i] << (i + 1 == n ? '\n' : ' ');
    return 0;
}
