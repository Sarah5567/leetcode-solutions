class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = (int)citations.size();
        if (n == 0) return 0;

        if (citations[n - 1] == 0) return 0;
        if (citations[0] >= n) return n;

        int left = 0, right = n;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (mid == 0 || citations[n - mid] >= mid) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return right;
    }
};
