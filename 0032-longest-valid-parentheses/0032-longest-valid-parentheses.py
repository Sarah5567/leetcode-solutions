class Solution:
    def longestValidParentheses(self, s: str) -> int:
        openAndClose = [0] * len(s)
        maxLength = 0
        sum = 0
        length = 0

        for i in range(len(openAndClose)):
            openAndClose[i] = 1 if s[i] == '(' else -1
            sum = max(openAndClose[i] + sum, openAndClose[i])
            if sum >= 0:
                length += 1
                if sum == 0:
                    maxLength = max(maxLength, length)
            else:
                length = 0

        sum = 0
        length = 0
        for i in range(len(openAndClose) - 1, -1, -1):
            sum = min(openAndClose[i] + sum, openAndClose[i])
            if sum <= 0:
                length += 1
                if sum == 0:
                    maxLength = max(maxLength, length)
            else:
                length = 0

        return maxLength
