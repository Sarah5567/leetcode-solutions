class Solution {
private:
    unordered_map<int, vector<int>> valueToIndices;

    int random(int max) {
        static mt19937 gen(random_device{}());
        uniform_int_distribution<int> dist(0, max);
        return dist(gen);
    }

public:
    Solution(vector<int>& nums) {
        for(int i = 0; i < nums.size(); i++)
            this->valueToIndices[nums[i]].push_back(i);
    }
    
    int pick(int target) {
        auto& targetList = this->valueToIndices[target];
        int randomChoice = this->random(targetList.size() - 1);
        return targetList[randomChoice];
    }
};
