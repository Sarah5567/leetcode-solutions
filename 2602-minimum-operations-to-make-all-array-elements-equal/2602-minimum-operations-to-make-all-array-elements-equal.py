class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        prefix_sum = list(accumulate(nums))

        ans = [0] * len(queries)

        for i, query in enumerate(queries):
            first_index = bisect_left(nums, query)

            if first_index > 0:
                ans[i] = query * first_index - prefix_sum[first_index - 1]

            right_sum = prefix_sum[-1] - (prefix_sum[first_index - 1] if first_index > 0 else 0)
            ans[i] += right_sum - query * (n - first_index)
            
        return ans
            