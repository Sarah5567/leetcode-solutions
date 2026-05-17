class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        indexes = {}
        next_index = [0] * n

        for i in range(n - 1, - 1, -1):
            if rains[i]:
                next_index[i] = indexes[rains[i]] if rains[i] in indexes else n
                indexes[rains[i]] = i

        heap = []
        ans = [-1] * n
        for i in range(n):
            if rains[i]:
                if next_index[i] < n:
                    heapq.heappush(heap, next_index[i])

            elif not heap:
                ans[i] = 1
            elif heap[0] <= i:
                return []
            else:
                ans[i] = rains[heapq.heappop(heap)]

        return ans if not heap else []
