class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for bit in range(32):
            count_lsb_set = 0
            for i in range(len(nums)):
                count_lsb_set += (nums[i] & 1)
                nums[i] >>= 1
            
            if count_lsb_set % 3:
                ans |= 1 << bit

        if ans & (1 << 31):
            ans -= (1 << 32)

        return ans
        