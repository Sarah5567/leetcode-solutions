class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 2 and s[0] > s[1]:
            return -1

        max_val = 'a'
        min_val = 'z'
        count_min = 0
        count_max = 0
        is_sorted = True

        for i in range(len(s)):
            if s[i] > max_val:
                max_val = s[i]
                count_max = 1
            elif s[i] == max_val:
                count_max += 1

            if s[i] < min_val:
                min_val = s[i]
                count_min = 1
            elif s[i] == min_val:
                count_min += 1

            if i > 0 and s[i] < s[i - 1]:
                is_sorted = False

        if is_sorted:
            return 0
        elif s[0] == min_val or s[-1] == max_val:
            return 1
        elif s[0] != max_val or s[-1] != min_val or count_max > 1 or count_min > 1:
            return 2
        else:
            return 3
