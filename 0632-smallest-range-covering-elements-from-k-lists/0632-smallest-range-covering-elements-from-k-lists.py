import heapq
from typing import List

class ItemWithDetails:
    def __init__(self, value, arr, index):
        self.value = value
        self.arr = arr
        self.index = index

    def __lt__(self, other):
        return self.value < other.value

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        max_val = float('-inf')
        k = len(nums)

        for i in range(k):
            val = nums[i][0]
            max_val = max(max_val, val)
            heapq.heappush(min_heap, ItemWithDetails(val, i, 0))

        min_range = [min_heap[0].value, max_val]

        while True:
            curr_min = heapq.heappop(min_heap)
            if curr_min.index == len(nums[curr_min.arr]) - 1:
                break

            next_val = nums[curr_min.arr][curr_min.index + 1]
            max_val = max(max_val, next_val)
            heapq.heappush(min_heap, ItemWithDetails(next_val, curr_min.arr, curr_min.index + 1))

            curr_low = min_heap[0].value
            if min_range[1] - min_range[0] > max_val - curr_low:
                min_range = [curr_low, max_val]

        return min_range
