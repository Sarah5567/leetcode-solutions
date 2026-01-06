class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)    
        parity = nums[0] % 2

        next_index1, next_index2 = 0, 1
        minimum_swaps1, minimum_swaps2 = 0, 0

        for i, num in enumerate(nums):
            if num % 2 == parity:
                if next_index2 >= n:
                    minimum_swaps2 = n ** 2
                minimum_swaps1 += abs(i - next_index1)
                minimum_swaps2 += abs(i - next_index2)
                next_index1 += 2
                next_index2 += 2
        
        if not n - 1 < next_index1 < n + 2:
            minimum_swaps1 = n ** 2
        if not n - 1 < next_index2 < n + 2:
            minimum_swaps2 = n ** 2
        
        res = min(minimum_swaps1, minimum_swaps2)
        return res if res < n ** 2 else -1
         