class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = [1]
        sign = 1
        answer = 0
        index = 0

        while index < len(s):
            char = s[index]

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
                last_index = index
                while last_index + 1 < len(s) and s[last_index + 1].isdigit():
                    last_index += 1
                
                current_num = int(s[index:last_index + 1])
                answer += current_num * sign * stack[-1]
                
                index = last_index

            index += 1

        return answer