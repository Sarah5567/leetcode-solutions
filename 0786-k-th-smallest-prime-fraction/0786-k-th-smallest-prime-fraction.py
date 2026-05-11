class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        last_denominator = [n - 1] * (n - 1)

        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (arr[i]/arr[-1], i, n - 1))

        for _ in range(k):
            val, i, j = heapq.heappop(heap)
            last_denominator[i] -= 1
            heapq.heappush(heap, (arr[i]/arr[last_denominator[i]], i, last_denominator[i]))

        return [arr[i], arr[j]]
