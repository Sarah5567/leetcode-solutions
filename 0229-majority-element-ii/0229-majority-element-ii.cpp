class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n = nums.size();
        vector<int> majorities = {-1, -1};
        vector<int> counts = {0, 0};

        for(int i = 0; i < n; i++){
            if(nums[i] == majorities[0])
                counts[0]++;
            else if(nums[i] == majorities[1])
                counts[1]++;
            else{
                if(counts[0] <= 0){
                    majorities[0] = nums[i];
                    counts[0] = 1; 
                }
                else if(counts[1] <= 0){
                    majorities[1] = nums[i];
                    counts[1] = 1;
                }
                else{
                    counts[0]--;
                    counts[1]--;
                }
            }
        }
        counts = {0, 0};
        for(int i = 0; i < n; i++){
            if(nums[i] == majorities[0])
                counts[0]++;
            else if(nums[i] == majorities[1])
                counts[1]++;
        }

        if(counts[0] <= n / 3)
            majorities.erase(majorities.begin());
        if(counts[1] <= n / 3)
            majorities.pop_back();
        
        return majorities;
    }
};