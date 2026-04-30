class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)

        indexes = [i for i in range(n)]
        indexes.sort(key=lambda i:capital[i])

        total_capital = w
        last_index = 0

        heap = []

        for _ in range(k):
            while last_index < n and capital[indexes[last_index]] <= total_capital:
                heapq.heappush(heap, -profits[indexes[last_index]])
                last_index += 1

            if not heap:
                break
            
            total_capital += -heapq.heappop(heap)

        return total_capital


