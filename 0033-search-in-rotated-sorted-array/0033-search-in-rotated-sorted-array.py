class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif (nums[mid] < target <= nums[right]) or (nums[right] < nums[mid] and (target <= nums[right] or target > nums[mid])):
                left = mid + 1
            else:
                right = mid - 1

        return -1
