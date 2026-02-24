class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        balance = defaultdict(int)
        chunks = 0
        nonzero = 0

        for a, b in zip(arr, sorted_arr):
            # עדכון הערך a
            balance[a] -= 1
            if balance[a] == 0:
                nonzero -= 1
            elif balance[a] == -1:
                nonzero += 1

            balance[b] += 1
            if balance[b] == 0:
                nonzero -= 1
            elif balance[b] == 1:
                nonzero += 1

            if nonzero == 0:
                chunks += 1

        return chunks