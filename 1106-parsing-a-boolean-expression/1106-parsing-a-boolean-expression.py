class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        idx = 0
        n = len(expression)

        def skip_to_matching_close():
            nonlocal idx
            depth = 0
            while idx < n:
                if expression[idx] == '(':
                    depth += 1
                elif expression[idx] == ')':
                    if depth == 0:
                        return
                    depth -= 1
                idx += 1

        def parse_sub_expression() -> bool:
            nonlocal idx

            ch = expression[idx]
            if ch == 't':
                idx += 1
                return True
            if ch == 'f':
                idx += 1
                return False

            if ch == '!':
                idx += 2
                val = parse_sub_expression()
                idx += 1
                return not val

            if ch == '&':
                idx += 2
                val = True
                while expression[idx] != ')':
                    val = val and parse_sub_expression()
                    if not val:
                        skip_to_matching_close()
                        break
                    if expression[idx] == ',':
                        idx += 1
                idx += 1
                return val

            if ch == '|':
                idx += 2
                val = False
                while expression[idx] != ')':
                    val = val or parse_sub_expression()
                    if val:
                        skip_to_matching_close()
                        break
                    if expression[idx] == ',':
                        idx += 1
                idx += 1  # skip ')'
                return val

            raise ValueError(f"Unexpected char: {expression[idx]} at {idx}")

        return parse_sub_expression()