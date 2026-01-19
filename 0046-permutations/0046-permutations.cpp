class Solution {
public:
    void allPermutation(vector<int>& nums, vector<vector<int>>& res, vector<int>& permutation, unsigned mask, int idx){
        if(idx == nums.size()){
            res.push_back(permutation);
            return;
        }
        for(int i = 0; i < nums.size(); i++){
            if(!((mask >> i) & 1)){
                permutation[idx] = nums[i];
                allPermutation(nums, res, permutation, mask | (1 << i), idx + 1);
            }
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> permutation(nums.size());
        allPermutation(nums, res, permutation, 0, 0);
        return res;
    }
};