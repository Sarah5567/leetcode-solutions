class Solution {
private:
    int mergeSort(vector<long long>& pref, int l, int r, int lower, int upper){
        int n = r - l;
        if (n <= 1) return 0;

        int mid = l + (r - l) / 2;
        int res = mergeSort(pref, l, mid, lower, upper);
        res += mergeSort(pref, mid, r, lower, upper);

        vector<long long> merged(n);

        int lowerBound = l, upperBound = l;
        int leftIdx = l, rightIdx = mid;
    
        for(int i = 0; i < n; i++){
            if(rightIdx < r && (leftIdx == mid || pref[rightIdx] > pref[leftIdx])){
                while (lowerBound < mid && pref[rightIdx] - pref[lowerBound] < lower) lowerBound++;
                while (upperBound < mid && pref[rightIdx] - pref[upperBound] <= upper) upperBound++;
                res += (upperBound - lowerBound);

                merged[i] = pref[rightIdx++];
            }
            else
                merged[i] = pref[leftIdx++];
        }

        for(int i = 0, j = l; i < n; i++, j++)
            pref[j] = merged[i];

        return res;
    }
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int n = nums.size();

        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; i++)
            pref[i + 1] = pref[i] + (long long)nums[i];

        return mergeSort(pref, 0, n + 1, lower, upper);
    }
};