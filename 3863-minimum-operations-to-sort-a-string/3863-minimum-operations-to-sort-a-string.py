class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if n == 2 and s[0] > s[1]:
            return -1

        max_val = 'a'
        min_val = 'z'
        count_min = 0
        count_max = 0
        is_sorted = True

        prev = s[0]

        for i in range(n):
            c = s[i]

            if c > max_val:
                max_val = c
                count_max = 1
            elif c == max_val:
                count_max += 1

            if c < min_val:
                min_val = c
                count_min = 1
            elif c == min_val:
                count_min += 1

            if is_sorted and i > 0 and c < prev:
                is_sorted = False

            prev = c

        if is_sorted:
            return 0
        elif s[0] == min_val or s[-1] == max_val:
            return 1
        elif s[0] != max_val or s[-1] != min_val or count_max > 1 or count_min > 1:
            return 2
        else:
            return 3
        