class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        heap = []
        score = 0
        suffix_damage = 0

        for i in range(n - 1, - 1, -1):
            heapq.heappush(heap, -(requirement[i] - suffix_damage))
            suffix_damage += damage[i]
            
            while heap and -heap[0] > hp - suffix_damage:
                heapq.heappop(heap)

            score += len(heap)

        return score
