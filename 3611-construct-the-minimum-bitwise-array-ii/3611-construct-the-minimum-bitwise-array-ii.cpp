class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n);

        for(int i  = 0; i < n; i++){
            if(nums[i] == 2)
                ans[i] = -1;
            else{
                int shift;
                for(shift = 0; (nums[i] >> shift) & 1; shift++);
                shift--;

                ans[i] = ~(1 << shift) & nums[i];
            }

        }
        return ans;
    }
};