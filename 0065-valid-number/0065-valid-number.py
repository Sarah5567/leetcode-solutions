class Solution:
    def followed_by_or_follow_digit(self, s : str, index : int):
        if index > 0 and s[index - 1].isdigit():
            return True
        elif index < len(s) - 1 and s[index + 1].isdigit():
            return True
        else:
            return False

    def isNumber(self, s: str) -> bool:
        has_dot : bool = False
        has_e : bool = False
        has_digit : bool = False
        
        for i, c in enumerate(s):
            if c.isdigit():
                has_digit = True
            elif c == '.':
                if has_dot or not self.followed_by_or_follow_digit(s, i):
                    return False
                else:
                    has_dot = True
            elif c in ['E', 'e']:
                if has_e or not has_digit:
                    return False
                else:
                    has_e = has_dot = True
                    has_digit = False
            elif c in ['+', '-']:
                if i > 0 and s[i - 1] not in ['E', 'e']:
                    return False
            else:
                return False
        
        return has_digit