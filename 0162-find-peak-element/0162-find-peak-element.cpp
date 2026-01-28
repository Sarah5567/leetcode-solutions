class Solution {
private:
    bool isPeak(vector<int>& nums, int i){
        if(i > 0 && nums[i] < nums[i - 1])
            return false;
        return i == nums.size() - 1 || nums[i] > nums[i + 1];
    }
public:
    int findPeakElement(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        int mid = left + (right - left) / 2;

        while(!isPeak(nums, mid)){
            if(mid < nums.size() - 1 && nums[mid] < nums[mid + 1])
                left = mid + 1;
            else
                right = mid - 1;
            mid = left + (right - left) / 2;
        }
        return mid;
    }
};