class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        positive = negetive = nums[0]
        product = nums[0]
        for num in nums[1:]:
            if num < 0:
                positive, negetive = negetive, positive

            positive = max(num, positive * num)
            negetive = min(num, negetive * num)

            product = max(product, positive)

        return product
            

