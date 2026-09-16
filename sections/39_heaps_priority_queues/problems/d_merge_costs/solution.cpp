#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n))
        return 0;

    priority_queue<
        long long,
        vector<long long>,
        greater<long long>
    > heap;

    for (int i = 0; i < n; ++i) {
        long long size;
        cin >> size;
        heap.push(size);
    }

    long long answer = 0;
    while (heap.size() > 1) {
        long long first = heap.top();
        heap.pop();

        long long second = heap.top();
        heap.pop();

        long long merged = first + second;
        answer += merged;
        heap.push(merged);
    }

    cout << answer << '\n';
    return 0;
}
