class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def find_first_element(elem):
            left = 0
            right = n
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] >= elem and (mid == 0 or nums[mid - 1] < elem):
                    return mid
                elif nums[mid] < elem:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        first_idx = find_first_element(target)
        last_idx = find_first_element(target + 1) - 1
        if 0 <= first_idx < n and nums[first_idx] == target:
            return [first_idx, last_idx]
        else:
            return [-1, -1]
            
