#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k, target;
    cin >> n >> k >> target;
    vector<int> values(n);
    for (int& value : values) cin >> value;
    int middle = n / 2;
    vector<unordered_map<int, long long>> frequency(middle + 1);
    function<void(int, int, int)> collect = [&](int i, int used, int code) {
        if (used > k) return;
        if (i == middle) {
            ++frequency[used][code];
            return;
        }
        collect(i + 1, used, code);
        collect(i + 1, used + 1, code ^ values[i]);
    };
    function<long long(int, int, int)> combine = [&](
        int i, int used, int code) {
        if (used > k) return 0LL;
        if (i == n) {
            int need = k - used;
            if (need < 0 || need > middle) return 0LL;
            auto it = frequency[need].find(target ^ code);
            return it == frequency[need].end() ? 0LL : it->second;
        }
        return combine(i + 1, used, code)
             + combine(i + 1, used + 1, code ^ values[i]);
    };
    collect(0, 0, 0);
    cout << combine(middle, 0, 0) << '\n';
}
