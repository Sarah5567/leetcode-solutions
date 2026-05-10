class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n1, n2 = float('inf'), float('inf')

        for num in nums:
            if num > n2:
                return True
            elif num > n1:
                n2 = num
            else:
                n1 = num

        return False
