class Solution {
public:
    int minimumDistance(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> valuesIndexes(n + 1);

        for(int i = 0; i < n; i++)
            valuesIndexes[nums[i]].push_back(i);

        int minimumDist = INT_MAX;
        for(auto& indexes : valuesIndexes){
            for(int third = 2; third < indexes.size(); third++){
                int first = third - 2;
                int curDist = 2 * indexes[third] - 2 * indexes[first];
                minimumDist = min(minimumDist, curDist);
            }
        }

        return minimumDist == INT_MAX ? -1 : minimumDist;
    }
};