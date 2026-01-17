class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {
        set<long long> s;
        for(int i = 0; i < nums.size(); i++){
            if(i > indexDiff)
                s.erase(nums[i - indexDiff - 1]);

            long long curVal = nums[i];

            auto next = s.lower_bound(curVal);
            if (next != s.end() && *next - curVal <= valueDiff)
                return true;

            if (next != s.begin()) {
                auto prev = next;
                --prev;
                if (curVal - *prev <= valueDiff)
                    return true;
            }

            s.insert(nums[i]);
        }
        return false;
    }
};