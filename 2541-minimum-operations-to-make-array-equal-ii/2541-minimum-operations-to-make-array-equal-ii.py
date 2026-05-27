class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if not k:
            return 0 if nums1 == nums2 else -1

        count_increases = 0
        count_decreases = 0

        for num1, num2 in zip(nums1, nums2):
            diff = num2 - num1
            if diff % k:
                return -1
            elif diff > 0:
                count_increases += diff // k
            else:
                count_decreases += (-diff) // k

        return count_increases if count_increases == count_decreases else -1
        