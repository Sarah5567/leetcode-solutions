class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)

        indexes = list(range(n))
        indexes.sort(key=lambda i:nums1[i])

        heap = []
        answer = [0] * n
        max_sum = 0

        i = 0
        while i < n:
            val = nums1[indexes[i]]
            next_max_sum = max_sum

            while i < n and nums1[indexes[i]] == val:
                heapq.heappush(heap, nums2[indexes[i]])
                next_max_sum += nums2[indexes[i]]
                if len(heap) > k:
                    next_max_sum -= heapq.heappop(heap)

                answer[indexes[i]] = max_sum
                i += 1

            max_sum = next_max_sum

        return answer
                

