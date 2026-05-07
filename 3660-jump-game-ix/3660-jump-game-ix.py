class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        min_suffix = [0] * n
        min_suffix[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(nums[i], min_suffix[i + 1])

        max_prefix = nums[0]
        begin = 0
        segment_max = nums[0]

        ans = [0] * n

        for i in range(1, n):
            if max_prefix <= min_suffix[i]:
                for j in range(begin, i):
                    ans[j] = segment_max

                begin = i
                segment_max = ans[i]

            max_prefix = max(max_prefix, nums[i])
            segment_max = max(segment_max, nums[i])

        for i in range(begin, n):
            ans[i] = segment_max

        return ans
