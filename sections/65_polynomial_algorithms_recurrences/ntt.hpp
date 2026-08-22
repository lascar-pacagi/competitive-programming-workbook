#pragma once
#include <algorithm>
#include <cstdint>
#include <vector>

namespace course_ntt {

constexpr int MOD = 998244353;
constexpr int ROOT = 3;

inline int power(long long base, long long exponent) {
    long long result = 1;
    while (exponent > 0) {
        if (exponent & 1) result = result * base % MOD;
        base = base * base % MOD;
        exponent >>= 1;
    }
    return static_cast<int>(result);
}

inline void transform(std::vector<int> &a, bool inverse) {
    int n = static_cast<int>(a.size());
    for (int i = 1, j = 0; i < n; ++i) {
        int bit = n >> 1;
        while (j & bit) {
            j ^= bit;
            bit >>= 1;
        }
        j ^= bit;
        if (i < j) std::swap(a[i], a[j]);
    }

    for (int length = 2; length <= n; length <<= 1) {
        int root = power(ROOT, (MOD - 1) / length);
        if (inverse) root = power(root, MOD - 2);
        for (int start = 0; start < n; start += length) {
            long long current = 1;
            for (int offset = 0; offset < length / 2; ++offset) {
                int left = a[start + offset];
                int right = static_cast<int>(
                    current * a[start + offset + length / 2] % MOD
                );
                a[start + offset] = left + right;
                if (a[start + offset] >= MOD) a[start + offset] -= MOD;
                a[start + offset + length / 2] = left - right;
                if (a[start + offset + length / 2] < 0)
                    a[start + offset + length / 2] += MOD;
                current = current * root % MOD;
            }
        }
    }

    if (inverse) {
        int inverse_n = power(n, MOD - 2);
        for (int &value : a)
            value = static_cast<int>(1LL * value * inverse_n % MOD);
    }
}

inline std::vector<int> convolution(
    const std::vector<int> &a,
    const std::vector<int> &b,
    int keep = -1
) {
    if (a.empty() || b.empty()) return {};
    int result_size = static_cast<int>(a.size() + b.size() - 1);
    if (keep >= 0) result_size = std::min(result_size, keep);
    if (std::min(a.size(), b.size()) <= 24) {
        std::vector<int> result(result_size);
        for (int i = 0; i < static_cast<int>(a.size()); ++i)
            for (int j = 0; j < static_cast<int>(b.size()) && i + j < result_size; ++j)
                result[i + j] = (result[i + j] + 1LL * a[i] * b[j]) % MOD;
        return result;
    }
    int size = 1;
    while (size < static_cast<int>(a.size() + b.size() - 1)) size <<= 1;
    std::vector<int> left(a.begin(), a.end()), right(b.begin(), b.end());
    left.resize(size);
    right.resize(size);
    transform(left, false);
    transform(right, false);
    for (int i = 0; i < size; ++i)
        left[i] = static_cast<int>(1LL * left[i] * right[i] % MOD);
    transform(left, true);
    left.resize(result_size);
    return left;
}

}  // namespace course_ntt
