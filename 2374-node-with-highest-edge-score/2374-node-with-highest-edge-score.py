class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        scores = [0] * n

        for i, edge in enumerate(edges):
            scores[edge] += i

        return scores.index(max(scores))
