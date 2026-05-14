class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ''
        for row in range(numRows):
            cur_jump = 2 * (numRows - row - 1)
            next_jump = 2 * row

            index = row
            while index < len(s):
                ans +=  s[index]
                
                index += max(cur_jump if cur_jump else next_jump, 1)
                cur_jump, next_jump = next_jump, cur_jump

        return ans
            