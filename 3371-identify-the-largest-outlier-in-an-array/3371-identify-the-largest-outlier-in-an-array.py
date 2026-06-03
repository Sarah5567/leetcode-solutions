class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        largest_outlier = float('-inf')
        counter = Counter(nums)
        total_sum = sum(nums)

        for num, count in counter.items():
            outlier = total_sum - num * 2
            if outlier in counter and (num != outlier or count > 1):
                largest_outlier = max(largest_outlier, outlier)

        return largest_outlier
