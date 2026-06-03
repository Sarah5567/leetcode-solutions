class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) > k * 2:
            return True

        mods = {0:-1}
        prefix_mod = 0

        for i, num in enumerate(nums):
            prefix_mod = (prefix_mod + num) % k
            if prefix_mod in mods:
                if mods[prefix_mod] < i - 1:
                    return True

            else:
                mods[prefix_mod] = i

        return False