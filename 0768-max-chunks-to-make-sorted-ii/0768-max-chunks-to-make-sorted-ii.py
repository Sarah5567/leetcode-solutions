class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        balance = Counter()
        chunks = 0

        for a, b in zip(arr, sorted_arr):
            balance[a] -= 1
            balance[b] += 1

            for key in (a, b):
                if balance[key] == 0:
                    del balance[key]

            if not balance:
                chunks += 1

        return chunks