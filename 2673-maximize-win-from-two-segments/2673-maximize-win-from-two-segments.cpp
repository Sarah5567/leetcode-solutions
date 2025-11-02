class Solution {
public:
    int maximizeWin(vector<int>& prizePositions, int k) {
        int n = prizePositions.size();
        if (n == 0) return 0;

        vector<int> maxFirstSegment(n);
        int left = 0;

        for (int right = 0; right < n; right++) {
            while (prizePositions[right] - prizePositions[left] > k)
                left++;
            int len = right - left + 1;
            maxFirstSegment[right] = (right > 0 ? max(maxFirstSegment[right - 1], len) : len);
        }

        int ans = 0;
        left = 0;
        for (int right = 0; right < n; right++) {
            while (prizePositions[right] - prizePositions[left] > k)
                left++;
            int len = right - left + 1;
            int prev = (left > 0 ? maxFirstSegment[left - 1] : 0);
            ans = max(ans, len + prev);
        }

        return ans;
    }
};
