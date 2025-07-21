class Solution {
public:
    bool xorGame(vector<int>& nums) {
        int xorN = 0;
        for(auto n : nums)
            xorN ^= n;
        return !xorN || !(nums.size() % 2);
    }
};