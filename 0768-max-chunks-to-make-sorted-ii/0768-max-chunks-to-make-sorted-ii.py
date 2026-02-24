class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        seen = defaultdict(int)
        length = 0
        chunks = 0

        for val, sorted_val in zip(arr, sorted_arr):
            length += 1

            seen[sorted_val] += 1
            if not seen[sorted_val]:
                del seen[sorted_val]

            seen[val] -= 1
            if not seen[val]:
                del seen[val]

            if not seen:
                chunks += 1

        return chunks
