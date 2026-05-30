class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        cost = nums.copy()
        best = sum(nums)

        for i in range(1, n):
            total_cost = 0
            for j in range(n):
                cost[j] = min(cost[j], nums[(j + i) % n])
                total_cost += cost[j]

            best = min(best, total_cost + x * i)

        return best 
