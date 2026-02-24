class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        seen = defaultdict(int)
        chunks = 0
        nonzero = 0

        for val, sorted_val in zip(arr, sorted_arr):

            seen[sorted_val] += 1
            if seen[sorted_val] == 1:
                nonzero += 1
            if seen[sorted_val] == 0:
                nonzero -= 1

            seen[val] -= 1
            if seen[val] == -1:
                nonzero += 1
            if seen[val] == 0:
                nonzero -= 1

            if not nonzero:
                chunks += 1

        return chunks
