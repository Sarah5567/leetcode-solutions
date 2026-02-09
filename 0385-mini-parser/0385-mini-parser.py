class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        n = len(s)
        ZERO = ord('0')

        def parse(idx: int):
            if s[idx] == ',':
                idx += 1

            c = s[idx]
            if c == '-' or ('0' <= c <= '9'):
                sign = 1
                if c == '-':
                    sign = -1
                    idx += 1

                value = 0
                while idx < n and ('0' <= s[idx] <= '9'):
                    value = value * 10 + (ord(s[idx]) - ZERO)
                    idx += 1

                return NestedInteger(sign * value), idx

            obj = NestedInteger()
            idx += 1
            lst = obj.getList()
            while s[idx] != ']':
                sub, idx = parse(idx)
                lst.append(sub)
            return obj, idx + 1

        obj, _ = parse(0)
        return obj
