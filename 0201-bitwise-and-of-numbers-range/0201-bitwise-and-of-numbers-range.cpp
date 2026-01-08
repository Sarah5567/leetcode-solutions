class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int bit = 0;

        while (left != right) {
            left >>= 1;
            right >>= 1;
            bit++;
        }

        return left << bit;
    }
};
