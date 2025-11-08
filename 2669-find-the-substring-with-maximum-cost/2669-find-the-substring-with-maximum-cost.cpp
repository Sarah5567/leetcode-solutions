class Solution {
public:
    int maximumCostSubstring(string s, string chars, vector<int>& vals) {
        const int ALPHABET_SIZE = 26;
        vector<int> cost(ALPHABET_SIZE);
        iota(cost.begin(), cost.end(), 1);

        for(int i = 0; i < chars.size(); i++){
            cost[chars[i] - 'a'] = vals[i];
        }

        int maxSum = 0;
        int curSum = 0;
        int minSum = 0;
        int minIndex = -1;
        for(int i = 0; i < s.length(); i++){
            curSum += cost[s[i] - 'a'];
            if(curSum < minSum){
                minSum = curSum;
                minIndex = i;
            }
            else if(maxSum < curSum - minSum){
                maxSum = curSum - minSum;
            }
        }

        return maxSum;       
    }
};
