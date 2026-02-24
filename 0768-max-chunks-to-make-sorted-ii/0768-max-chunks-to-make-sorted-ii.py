class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        balance = defaultdict(int)
        chunks = 0

        for a, b in zip(arr, sorted_arr):
            balance[a] -= 1
            balance[b] += 1

            if balance[a] == 0:
                del balance[a]
            if balance[b] == 0:
                del balance[b]

            if not balance:
                chunks += 1

        return chunks