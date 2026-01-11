class Solution {
public:
    int divide(int dividend, int divisor) {
        // Special overflow case: INT_MIN / -1 = 2147483648 -> clamp to INT_MAX
        if (dividend == INT_MIN && divisor == -1) return INT_MAX;

        // Work in long long to avoid overflow on abs(INT_MIN)
        long long a = dividend;
        long long b = divisor;

        bool negative = (a < 0) ^ (b < 0);
        a = llabs(a);
        b = llabs(b);

        long long ans = 0;

        // Build quotient using largest doubled divisor each time
        while (a >= b) {
            long long temp = b;
            long long mult = 1;

            // Double temp until next doubling would exceed a
            while ((temp << 1) <= a) {
                temp <<= 1;
                mult <<= 1;
            }

            a -= temp;
            ans += mult;
        }

        if (negative) ans = -ans;

        // Clamp (shouldn't be needed except overflow case already handled, but safe)
        if (ans > INT_MAX) return INT_MAX;
        if (ans < INT_MIN) return INT_MIN;
        return (int)ans;
    }
};
