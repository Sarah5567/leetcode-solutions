class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curBorder = 1
        nextBorder = 1

        i = 0
        n = len(nums)

        # avoid repeated attribute lookups and range allocations
        while i < n:
            if i == curBorder:
                jumps += 1
                curBorder = nextBorder
            # store locally to avoid repeated nums[i] lookup
            val = nums[i]
            nb = i + val + 1
            if nb > nextBorder:
                nextBorder = nb
            i += 1

        return jumps
