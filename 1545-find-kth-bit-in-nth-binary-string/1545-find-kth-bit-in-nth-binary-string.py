class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(k, n):
            if n == 1:
                return '0'

            length = 2**n - 1
            mid = 2**(n - 1)

            if k == mid:
                return '1'
            elif k < mid:
                return helper(k, n - 1)
            else:
                new_k = length - k + 1
                bit = helper(new_k, n - 1)
                return '0' if bit == '1' else '1'

        return helper(k, n)