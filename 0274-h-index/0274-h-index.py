class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations) + 1
        count_citations = [0] * n

        for citation in citations:
            count_citations[min(citation, n - 1)] += 1

        suffix_sum = 0
        for i in range(n - 1, -1, -1):
            suffix_sum += count_citations[i]
            if i <= suffix_sum:
                return i

        return 0
