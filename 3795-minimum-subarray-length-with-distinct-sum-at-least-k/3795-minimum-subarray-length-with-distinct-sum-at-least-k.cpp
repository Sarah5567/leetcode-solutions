class Solution {
public:
    int minLength(vector<int>& nums, int k) {
            unordered_map<int, int> table;

            int shortest = INT_MAX, sum = 0;
            int l = 0;

            for(int r = 0; r < nums.size(); r++){
                if(table.find(nums[r]) != table.end() && table[nums[r]]){
                    table[nums[r]]++;
                    continue;
                }

                table[nums[r]] = 1;
                sum += nums[r];

                while(table[nums[l]] > 1 || sum - nums[l] >= k){
                    table[nums[l]]--;
                    if(!table[nums[l]]){
                        sum -= nums[l];
                    }
                    l++;
                }

                if(sum >= k)
                    shortest = min(shortest, r - l + 1);
            }

            if(shortest == INT_MAX)
                shortest = -1;
            return shortest;
    }
};