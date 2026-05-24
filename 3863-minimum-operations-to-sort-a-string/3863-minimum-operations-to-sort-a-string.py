class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 2 and s[0] > s[1]:
            return -1

        max_val = 'a'
        min_val = 'z'
        is_sorted = True

        for i in range(len(s)):
            max_val = max(max_val, s[i])
            min_val = min(min_val, s[i])
            if i > 0 and s[i] < s[i - 1]:
                is_sorted = False

        if is_sorted:
            return 0
        elif s[0] == min_val or s[-1] == max_val:
            return 1
        elif s[0] != max_val or s[-1] != min_val or s.count(max_val) > 1 or s.count(min_val) > 1:
            return 2
        else:
            return 3
