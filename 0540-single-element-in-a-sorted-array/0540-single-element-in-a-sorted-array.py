class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if mid % 2:
                mid -= 1

            if mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                left = mid + 2
            elif mid != 0 and nums[mid - 1] == nums[mid]:
                right = mid - 2
            else:
                return nums[mid]
        
        return -1
