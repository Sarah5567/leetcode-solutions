class Solution {
public:
    int maxDistinctElements(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());

        int curNum = nums[0] - k - 1;
        int countDistinctElements = 0;
        
        for (auto& num : nums){
            if(curNum <= num - 1)
                num = max(curNum + 1, num - k);
            else
                num = min(curNum + 1, num + k);
            
            if(num != curNum)
                countDistinctElements++;
            curNum = num;
        }
        return countDistinctElements;
    }
};