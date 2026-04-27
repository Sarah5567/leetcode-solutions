class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1
        
        subarrays = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            subarrays += sums[prefix_sum - k]
            sums[prefix_sum] += 1

        return subarrays
