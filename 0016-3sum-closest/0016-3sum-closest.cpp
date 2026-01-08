class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int n = nums.size();
        int closest_sum = nums[0] + nums[1] + nums[2];

        sort(nums.begin(), nums.end());

        for(int i = 0; i < n; i++){
            int left = i > 0 ? 0 : 1;
            int right = i < n - 1 ? n - 1 : n - 2;
            while(left < right){
                int cur_sum = nums[i] + nums[left] + nums[right];
                if(abs(target - closest_sum) > abs(target - cur_sum))
                    closest_sum = cur_sum;
                 
                if(cur_sum > target){
                    right--;
                    if(right == i)
                        right--;
                }
                else{
                    left++;
                    if(left == i)
                        left++;
                }
            }
        }
        return closest_sum;
    }
};