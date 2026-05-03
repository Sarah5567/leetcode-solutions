class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        numbers = []
        ops = []
        index = 0

        while index < len(s):
            if s[index] == '(':
               ops.append('(')

            elif s[index] == ')':
                operands = []
                while ops[-1] != '(':
                    last_op = ops.pop()
                    operands.append(numbers.pop() * (-1 if last_op == '-' else 1))
                ops.pop()
                numbers[-1] += sum(operands)

            elif s[index] in ['+', '-']:
                if index == 0 or s[index - 1] == '(':
                    numbers.append(0)
                ops.append(s[index])

            else:
                last_index = index
                while last_index + 1 < len(s) and s[last_index + 1].isdigit():
                    last_index += 1
            
                numbers.append(int(s[index:last_index + 1])) 
                index = last_index

            index += 1

        operands = []
        while ops:
            last_op = ops.pop()
            operands.append(numbers.pop() * (-1 if last_op == '-' else 1))
        return numbers[-1] + sum(operands)
