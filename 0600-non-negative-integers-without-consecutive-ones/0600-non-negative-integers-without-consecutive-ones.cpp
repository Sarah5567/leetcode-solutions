class Solution {
private:
    int getForLastOne(const vector<int>& zeroEnded, const vector<int>& oneEnded, int n, int i) {
        if (i <= 0) return 1;

        int nextOne = -1;
        for (int j = i - 1; j >= 0; --j) {
            if (((n >> j) & 1) != 0) {
                nextOne = j;
                break;
            }
        }

        if (nextOne == -1) return 1;
        if (nextOne + 1 == i) return oneEnded[i];
        return zeroEnded[nextOne] + getForLastOne(zeroEnded, oneEnded, n, nextOne);
    }

public:
    int findIntegers(int n) {
        if (n == 0) return 1;

        int bitWidth = 32 - __builtin_clz((unsigned)n);

        vector<int> zeroEnded(bitWidth, 0);
        vector<int> oneEnded(bitWidth, 0);

        zeroEnded[0] = oneEnded[0] = 1;

        for (int i = 1; i < bitWidth; i++) {
            zeroEnded[i] = zeroEnded[i - 1] + oneEnded[i - 1];
            oneEnded[i]  = zeroEnded[i - 1];
        }

        int res = getForLastOne(zeroEnded, oneEnded, n, bitWidth - 1);
        res += zeroEnded[bitWidth - 1];

        return res;
    }
};
