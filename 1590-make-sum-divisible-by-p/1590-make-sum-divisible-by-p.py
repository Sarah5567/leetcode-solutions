class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        mod = sum(nums) % p
        if not mod:
            return 0

        mods_dict = {0 : -1}

        prefix_mod = 0
        best = len(nums)

        for i, num in enumerate(nums):
            prefix_mod = (prefix_mod + num) % p
            target = (prefix_mod - mod) % p

            if target in mods_dict:
                best = min(best, i - mods_dict[target])
            mods_dict[prefix_mod] = i

        return best if best < len(nums) else -1
