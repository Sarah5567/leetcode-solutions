class Solution:
    def deserialize_from_idx(self, s: str, idx: int) -> tuple(NestedInteger, int):
        if s[idx] == ',':
            idx += 1

        if s[idx] == '-' or s[idx].isdigit():
            end = next((j for j in range(idx + 1, len(s)) if not s[j].isdigit()), len(s))
            num = int(s[idx:end])
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