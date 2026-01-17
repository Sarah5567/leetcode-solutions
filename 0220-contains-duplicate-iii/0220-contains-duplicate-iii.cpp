class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {
        set<long long> s;
        for(int i = 0; i < nums.size(); i++){
            if(i > indexDiff)
                s.erase(nums[i - indexDiff - 1]);

            long long curVal = nums[i];

            auto it = s.lower_bound(curVal - valueDiff);
            if (it != s.end() && *it <= curVal + valueDiff)
                return true;

            s.insert(nums[i]);
        }
        return false;
    }
};