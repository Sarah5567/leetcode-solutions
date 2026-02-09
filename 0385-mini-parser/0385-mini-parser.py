class Solution:
    def deserialize_from_idx(self, s: str, idx: int) -> tuple(NestedInteger, int):
        if s[idx] == ',':
            idx += 1

        if s[idx] == '-' or s[idx].isdigit():
            end = idx
            value = 0
            sign = 1

            if s[end] == '-':
                sign = -1
                end += 1

            while end < len(s) and s[end].isdigit():
                value = value * 10 + (ord(s[end]) - ord('0'))
                end += 1

            num = sign * value
            return NestedInteger(num), end
        
        else:
            obj = NestedInteger()
            idx += 1
            while s[idx] != ']':
                sub_obj, idx = self.deserialize_from_idx(s, idx)
                obj.getList().append(sub_obj)
            
            return obj, idx + 1

    def deserialize(self, s: str) -> NestedInteger:
        obj, idx = self.deserialize_from_idx(s, 0)
        return obj