class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        len1 = len2 = 1
        longest = 1

        for i in range(1, n):
            cur_len1 = 0
            if nums1[i - 1] <= nums1[i]:
                cur_len1 = len1
            if nums2[i - 1] <= nums1[i]:
                cur_len1 = max(cur_len1, len2)

            cur_len2 = 0
            if nums1[i - 1] <= nums2[i]:
                cur_len2 = len1
            if nums2[i - 1] <= nums2[i]:
                cur_len2 = max(cur_len2, len2)

            cur_len1 += 1
            cur_len2 += 1

            longest = max(longest, cur_len1, cur_len2)

            len1 = cur_len1
            len2 = cur_len2

        return longest