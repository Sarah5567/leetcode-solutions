class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        if(!nums.size())
            return 0;
        int sum = nums[0];
        int minimalLength = nums.size() + 1;
        int begin = 0, end = 0;

        while(end < nums.size()){
            if(sum >= target){
                minimalLength = min(minimalLength, end - begin + 1);
                if(begin < end){
                    sum -= nums[begin];
                    begin++;
                }
                else{
                    end++;
                    if(end < nums.size())
                        sum += nums[end];
                }
            }
            else{
                end++;
                if(end < nums.size())
                    sum += nums[end];
            }
        }

        if(minimalLength == nums.size() + 1)
            return 0;
        return minimalLength;
    }
};