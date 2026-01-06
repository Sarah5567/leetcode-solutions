class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<unsigned long long> countCombination(target + 1, 0);
        countCombination[0] = 1;
        for(int i = 0; i < target; i++){
            for(int num : nums){
                if(num + i <= target)
                    countCombination[num + i] += countCombination[i];
            }
        }
        return int(countCombination[target]);
    }
};