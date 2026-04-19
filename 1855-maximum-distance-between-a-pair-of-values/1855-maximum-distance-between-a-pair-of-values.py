class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_distance = 0
        i = 0
        for j in range(len(nums2)):
            while i < len(nums1) - 1 and nums1[i] > nums2[j]:
                i += 1

            if nums1[i] <= nums2[j]:
                max_distance = max(max_distance, j - i)

        return max_distance