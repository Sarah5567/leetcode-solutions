class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits_freq = [0] * 10
        arr_sum = 0

        for d in digits:
            digits_freq[d] += 1
            arr_sum += d

        def remove_digits(mod, k):
            for d in range(10):
                if d % 3 == mod:
                    while digits_freq[d] > 0 and k > 0:
                        digits_freq[d] -= 1
                        k -= 1
                        if k == 0:
                            return True
            return k == 0

        remainder = arr_sum % 3

        if remainder == 1:
            if not remove_digits(1, 1):
                remove_digits(2, 2)

        elif remainder == 2:
            if not remove_digits(2, 1):
                remove_digits(1, 2)

        res = []
        for d in range(9, -1, -1):
            res.extend([str(d)] * digits_freq[d])

        if not res:
            return ""

        if res[0] == '0':
            return "0"

        return "".join(res)