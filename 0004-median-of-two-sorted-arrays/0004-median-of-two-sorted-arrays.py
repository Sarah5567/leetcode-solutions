class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left < right:
            mid1 = left + (right - left) // 2
            mid2 = (m + n) // 2 - mid1

            if mid1 > 0 and mid2 < n and nums1[mid1 - 1] > nums2[mid2]:
                right = mid1 - 1

            elif mid2 > 0 and mid1 < m and nums2[mid2 - 1] > nums1[mid1]:
                left = mid1 + 1

            else:
                break

        mid1 = left + (right - left) // 2
        mid2 = (m + n) // 2 - mid1

        if (m + n) % 2:
            return min(nums1[mid1] if mid1 < m else float('inf'), nums2[mid2] if mid2 < n else float('inf'))
        else:
            if mid1 > 0 and (mid2 == 0 or nums1[mid1 - 1] > nums2[mid2 - 1]):
                smaller = nums1[mid1 - 1]
            else:
                smaller = nums2[mid2 - 1]

            if mid1 < m and (mid2 == n or nums1[mid1] < nums2[mid2]):
                greater = nums1[mid1]
            else:
                greater = nums2[mid2]

            return (smaller + greater) / 2
