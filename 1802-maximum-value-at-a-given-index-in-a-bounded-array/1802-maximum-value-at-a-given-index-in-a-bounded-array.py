class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def calc_sum(mid: int) -> int:
            total = mid
            
            left_len = index
            if mid > left_len:
                total += (mid - 1 + mid - left_len) * left_len // 2
            else:
                total += (mid - 1) * mid // 2
                total += left_len - (mid - 1)
            
            right_len = n - index - 1
            if mid > right_len:
                total += (mid - 1 + mid - right_len) * right_len // 2
            else:
                total += (mid - 1) * mid // 2
                total += right_len - (mid - 1)
            
            return total
        
        left, right = 1, maxSum
        
        while left <= right:
            mid = (left + right) // 2
            if calc_sum(mid) <= maxSum:
                left = mid + 1
            else:
                right = mid - 1
        
        return right
