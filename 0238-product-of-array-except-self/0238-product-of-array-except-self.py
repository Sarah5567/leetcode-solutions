class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        for i in range(1, len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]

        suffix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]

        return answer

        