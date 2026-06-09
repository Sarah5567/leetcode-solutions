class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = Counter(num % value for num in nums)

        ans = float('inf')

        for r in range(value):
            ans = min(ans, r + cnt[r] * value)

        return ans
        