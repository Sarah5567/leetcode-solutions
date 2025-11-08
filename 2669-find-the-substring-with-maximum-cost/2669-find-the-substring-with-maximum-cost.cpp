class Solution {
public:
    int maximumCostSubstring(const string& s, const string& chars, const vector<int>& vals) {
        static constexpr int ALPHABET_SIZE = 26;
        int cost[ALPHABET_SIZE];
        for (int i = 0; i < ALPHABET_SIZE; ++i)
            cost[i] = i + 1;

        for (int i = 0, n = chars.size(); i < n; ++i)
            cost[chars[i] - 'a'] = vals[i];

        int maxSum = 0;
        int curSum = 0;
        int minSum = 0;

        const unsigned char* str = reinterpret_cast<const unsigned char*>(s.data());
        for (int i = 0, n = s.size(); i < n; ++i) {
            curSum += cost[str[i] - 'a'];
            if (curSum < minSum)
                minSum = curSum;
            else if (curSum - minSum > maxSum)
                maxSum = curSum - minSum;
        }

        return maxSum;
    }
};
