class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        size = 1 << k # 2^k
        seen = [False] * size

        num = int(s[:k], 2)
        seen[num] = True     
        count_seen = 1

        mask = size - 1  

        for i in range(k, len(s)):
            if size - count_seen > len(s) - i:
                return False
            if count_seen == size:
                return True

            num = ((num << 1) & mask) | int(s[i])
            if not seen[num]:
                count_seen += 1
                seen[num] = True


        return count_seen == size