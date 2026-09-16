#include <bits/stdc++.h>
using namespace std;
using i128 = __int128_t;
using int64 = long long;

struct Machine {
    i128 a, start;
    int64 capacity;
};

void print_i128(i128 value) {
    if (value == 0) {
        cout << "0\n";
        return;
    }
    if (value < 0) {
        cout << '-';
        value = -value;
    }
    string digits;
    while (value) {
        digits.push_back(char('0' + value % 10));
        value /= 10;
    }
    reverse(digits.begin(), digits.end());
    cout << digits << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    int64 wanted;
    cin >> n >> wanted;
    vector<Machine> machines;
    i128 base_cost = 0;
    i128 minimum_total = 0;
    i128 maximum_total = 0;
    i128 search_low = 0, search_high = 0;
    bool has_extra = false;

    for (int i = 0; i < n; ++i) {
        int64 a_input, b_input, low, high;
        cin >> a_input >> b_input >> low >> high;
        i128 a = a_input;
        i128 b = b_input;
        base_cost += a * low * low + b * low;
        minimum_total += low;
        maximum_total += high;
        int64 capacity = high - low;
        if (!capacity) continue;
        i128 start = a * (2 * i128(low) + 1) + b;
        i128 last = start + 2 * a * (capacity - 1);
        machines.push_back({a, start, capacity});
        if (!has_extra) {
            search_low = start;
            search_high = last;
            has_extra = true;
        } else {
            search_low = min(search_low, start);
            search_high = max(search_high, last);
        }
    }

    if (wanted < minimum_total || wanted > maximum_total) {
        cout << "IMPOSSIBLE\n";
        return 0;
    }
    int64 need = wanted - int64(minimum_total);
    if (!need) {
        print_i128(base_cost);
        return 0;
    }

    auto count_at_most = [&](i128 threshold) {
        int64 count = 0;
        for (const Machine& machine : machines) {
            if (threshold < machine.start) continue;
            i128 raw = (threshold - machine.start)
                     / (2 * machine.a) + 1;
            int64 take = raw > machine.capacity
                       ? machine.capacity : int64(raw);
            if (count >= need - take) return need;
            count += take;
        }
        return count;
    };

    i128 left = search_low;
    i128 right = search_high;
    while (left < right) {
        i128 middle = left + (right - left) / 2;
        if (count_at_most(middle) >= need)
            right = middle;
        else
            left = middle + 1;
    }
    i128 threshold = left;

    int64 selected = 0;
    i128 answer = base_cost;
    for (const Machine& machine : machines) {
        if (threshold <= machine.start) continue;
        i128 raw = (threshold - 1 - machine.start)
                 / (2 * machine.a) + 1;
        int64 take = raw > machine.capacity
                   ? machine.capacity : int64(raw);
        selected += take;
        answer += i128(take) * machine.start
                + machine.a * take * (take - 1);
    }
    answer += i128(need - selected) * threshold;
    print_i128(answer);
}
