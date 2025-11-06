class Solution {
public:
    long long bowlSubarrays(vector<int>& nums) {
        stack<int> s;
        long long res = 0;

        for(int i = 0; i < nums.size(); i++){
            while(!s.empty() && nums[s.top()] < nums[i]){
                if(i - s.top() + 1 >= 3)
                    res++;
                s.pop();
            }

            if(!s.empty() && i - s.top() + 1 >= 3)
                res++;
            s.push(i);
        }

        return res;
    }
};