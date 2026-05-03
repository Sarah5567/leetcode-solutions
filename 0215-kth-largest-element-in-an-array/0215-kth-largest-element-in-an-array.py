class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            if len(min_heap) < k or num > min_heap[0]:
                heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]
