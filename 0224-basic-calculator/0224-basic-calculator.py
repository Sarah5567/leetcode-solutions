class Solution:
    def calculate(self, s: str) -> int:
        stack = [1]
        sign = 1
        answer = 0
        index = 0
        n = len(s)

        while index < n:
            char = s[index]

            if char == ' ':
                index += 1
                continue

            if char == '+':
                sign = 1
            elif char == '-':
                sign = -1
            elif char == '(':
                stack.append(sign * stack[-1])
                sign = 1
            elif char == ')':
                stack.pop()
            elif char.isdigit():
                num = 0
                while index < n and s[index].isdigit():
                    num = num * 10 + (ord(s[index]) - ord('0'))
                    index += 1

                answer += num * sign * stack[-1]
                index -= 1

            index += 1

        return answer
        