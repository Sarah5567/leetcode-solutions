class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        counts = Counter(arr)
        next_val = 1

        for val, count in sorted(counts.items()):
            next_val = min(val + 1, next_val + count)

        return next_val - 1
