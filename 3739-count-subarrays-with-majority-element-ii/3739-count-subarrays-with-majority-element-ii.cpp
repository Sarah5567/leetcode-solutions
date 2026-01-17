class Solution {
private:
    long long countWithMergeSort(vector<int>& nums, int l, int r) {
        if (l + 1 == r)
            return nums[l] > 0 ? 1 : 0;

        int mid = l + (r - l) / 2;
        long long res = 0;

        res += countWithMergeSort(nums, l, mid);
        res += countWithMergeSort(nums, mid, r);

        int leftSize = mid - l;
        int rightSize = r - mid;

        vector<long long> leftSuffix(leftSize);
        vector<long long> rightPrefix(rightSize);

        leftSuffix[0] = nums[mid - 1];
        for (int i = 1; i < leftSize; i++)
            leftSuffix[i] = leftSuffix[i - 1] + nums[mid - 1 - i];

        rightPrefix[0] = nums[mid];
        for (int i = 1; i < rightSize; i++)
            rightPrefix[i] = rightPrefix[i - 1] + nums[mid + i];

        sort(rightPrefix.begin(), rightPrefix.end());

        for (int i = 0; i < leftSize; i++) {
            long long j = upper_bound(
                rightPrefix.begin(),
                rightPrefix.end(),
                -leftSuffix[i]
            ) - rightPrefix.begin();

            res += rightSize - j;
        }

        return res;
    }

public:
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        for (int& x : nums)
            x = (x == target ? 1 : -1);

        return countWithMergeSort(nums, 0, nums.size());
    }
};
