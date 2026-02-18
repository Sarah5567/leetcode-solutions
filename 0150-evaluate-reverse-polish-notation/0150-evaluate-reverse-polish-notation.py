class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
                continue

            a = stack.pop()
            b = stack.pop()

            match token:
                case "+":
                    stack.append(b + a)
                case "-":
                    stack.append(b - a)
                case "*":
                    stack.append(b * a)
                case "/":
                    stack.append(int(b / a))  # truncate toward 0
        return stack[0]
