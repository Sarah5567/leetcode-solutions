class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        counts = Counter(arr)
        next_val = 1

        for val in sorted(counts):
            next_val = min(val + 1, next_val + counts[val])

        return next_val - 1
        