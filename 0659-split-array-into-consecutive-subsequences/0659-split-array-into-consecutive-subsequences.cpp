class Solution {
public:
    bool isPossible(std::vector<int>& nums) {
        if (nums.empty()) return true;

        int n = (int)nums.size();
        int countLen1 = 0, countLen2 = 0, countOptional = 0;

        int i = 0;
        int prevNum = nums[0] - 1;

        while (i < n) {
            int num = nums[i];

            if (num != prevNum + 1) {
                if (countLen1 || countLen2) return false;
                countOptional = 0;
            }

            int length = 1;
            while (i + length < n && nums[i + length] == nums[i]) length++;

            int remain = length - countLen1 - countLen2;
            if (remain < 0) return false;

            int useOptional = std::min(countOptional, remain);
            remain -= useOptional;
            countOptional = useOptional + countLen2;
            countLen2 = countLen1;
            countLen1 = remain;

            prevNum = num;
            i += length;
        }

        return countLen1 == 0 && countLen2 == 0;
    }
};
