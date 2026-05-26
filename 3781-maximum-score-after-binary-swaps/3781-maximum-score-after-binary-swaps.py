class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        ones = 0
        heap = []

        for i in range(len(s) - 1, -1, -1):
            ones += int(s[i])
            heapq.heappush(heap, nums[i])
            
            if len(heap) > ones:
                heapq.heappop(heap)

        return sum(heap)
        