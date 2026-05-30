class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        cost = nums[:]
        best = sum(nums)

        for i in range(1, n):
            curr = 0
            ni = nums
            ci = cost

            for j in range(n):
                v = ni[(j + i) % n]
                if v < ci[j]:
                    ci[j] = v
                curr += ci[j]

            candidate = curr + x * i
            if candidate < best:
                best = candidate

        return best
        