class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        push = stack.append
        pop = stack.pop

        for t in tokens:
            if t == '+':
                a = pop(); b = pop(); push(b + a)
            elif t == '-':
                a = pop(); b = pop(); push(b - a)
            elif t == '*':
                a = pop(); b = pop(); push(b * a)
            elif t == '/':
                a = pop(); b = pop(); push(int(b / a))
            else:
                push(int(t))

        return stack[0]
