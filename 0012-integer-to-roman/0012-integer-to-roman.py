class Solution:
    def intToRoman(self, num: int) -> str:
        pow10 = ['I', 'X', 'C', 'M']
        pow5 = ['V', 'L','D']

        num_s = str(num)
        ans = ''

        for i, ch in enumerate(num_s):
            pos = len(num_s) - i - 1

            match ch:
                case '9':
                    ans += pow10[pos] + pow10[pos + 1]
                case '4':
                    ans += pow10[pos] + pow5[pos]
                case _:
                    digit = int(ch)
                    if digit >= 5:
                        ans += pow5[pos]
                        digit -= 5
                    ans += pow10[pos] * digit

        return ans


