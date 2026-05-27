class Solution:
    def minimumOperations(self, num: str) -> int:
        found_zero = False
        found_five = False

        for i in range(len(num) - 1, -1, -1):
            if (found_zero and num[i] in ['5','0']) or (found_five and num[i] in ['2','7']):
                return len(num) - i - 2

            found_zero = found_zero or num[i] == '0'
            found_five = found_five or num[i] == '5'

        return len(num) - 1 if found_zero else len(num)
