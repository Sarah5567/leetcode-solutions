class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> lastElements(nums.size() + 1, INT_MAX);
        int maxLength = 0;

        for(auto& num : nums){
            auto it = lower_bound(lastElements.begin(), lastElements.begin() + maxLength + 1, num);
            int idx = int(it - lastElements.begin());

            lastElements[idx] = num;
            maxLength = max(maxLength, idx + 1);
        }

        return maxLength;
    }
};