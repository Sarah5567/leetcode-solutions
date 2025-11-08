class Solution {
public:
    int maximumCostSubstring(const string& s, const string& chars, const vector<int>& vals) {
        static constexpr int ALPHABET_SIZE = 26;
        int cost[ALPHABET_SIZE];
        for (int i = 0; i < ALPHABET_SIZE; ++i)
            cost[i] = i + 1;

        for (int i = 0; i < (int)chars.size(); ++i)
            cost[chars[i] - 'a'] = vals[i];

        int maxSum = 0;
        int curSum = 0;
        int minSum = 0;

        for (char c : s) {
            curSum += cost[c - 'a'];
            if (curSum < minSum)
                minSum = curSum;
            else if (maxSum < curSum - minSum)
                maxSum = curSum - minSum;
        }

        return maxSum;
    }
};
