class Solution:
    def get_invalid_close_positions(self, s: str) -> List[int]:
        invalid_close = []
        balance = 0

        for idx, ch in enumerate(s):
            if ch == '(':
                balance += 1
            elif ch == ')':
                if balance == 0:
                    invalid_close.append(idx)
                else:
                    balance -= 1

        return invalid_close
        
    def get_invalid_open_positions(self, s: str) -> List[int]:
        invalid_open = []
        balance = 0
        n = len(s)

        for i, ch in enumerate(reversed(s)):
            if ch == ')':
                balance += 1
            elif ch == '(':
                if balance == 0:
                    invalid_open.append(n - i - 1)
                else:
                    balance -= 1

        return invalid_open

    def get_valid_parentheses(
        self,
        s: str,
        origional: str,
        results: set,
        invalid_open: List[int],
        invalid_close: List[int],
        pos: int,
        s_pos: int,
        open_ptr: int,
        close_ptr: int
    ):
        n = len(origional)

        if pos == n:
            if open_ptr == -1 and close_ptr == len(invalid_close):
                results.add(s)
            return

        if close_ptr < len(invalid_close) and invalid_close[close_ptr] < pos:
            return

        if n - pos < open_ptr + 1:
            return

        if origional[pos] == '(' and open_ptr >= 0 and invalid_open[open_ptr] <= pos:
            self.get_valid_parentheses(
                s[:s_pos] + s[s_pos + 1:],
                origional,
                results,
                invalid_open,
                invalid_close,
                pos + 1,
                s_pos,
                open_ptr - 1,
                close_ptr
            )

        elif origional[pos] == ')' and close_ptr < len(invalid_close) and invalid_close[close_ptr] >= pos:
            self.get_valid_parentheses(
                s[:s_pos] + s[s_pos + 1:],
                origional,
                results,
                invalid_open,
                invalid_close,
                pos + 1,
                s_pos,
                open_ptr,
                close_ptr + 1
            )

        self.get_valid_parentheses(
            s,
            origional,
            results,
            invalid_open,
            invalid_close,
            pos + 1,
            s_pos + 1,
            open_ptr,
            close_ptr
        )

    def removeInvalidParentheses(self, s: str) -> List[str]:
        invalid_open = self.get_invalid_open_positions(s)
        invalid_close = self.get_invalid_close_positions(s)

        results = set()
        self.get_valid_parentheses(
            s,
            s,
            results,
            invalid_open,
            invalid_close,
            0,
            0,
            len(invalid_open) - 1,
            0
        )

        return list(results) if results else [""]
