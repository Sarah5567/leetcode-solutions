class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance_to_index = {0 : -1}
        balance, max_length  = 0, 0

        for i, num in enumerate(nums):
            balance += 1 if num else -1
            if balance in balance_to_index:
                max_length = max(max_length, i - balance_to_index[balance])
            else:
                balance_to_index[balance] = i

        return max_length
