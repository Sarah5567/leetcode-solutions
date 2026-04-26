class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):
                a = num[:i]
                b = num[i:j]

                if (a.startswith('0') and len(a) > 1) or (b.startswith('0') and len(b) > 1):
                    continue

                x, y = int(a), int(b)
                k = j

                while k < n:
                    z = x + y
                    z_str = str(z)

                    if not num.startswith(z_str, k):
                        break

                    k += len(z_str)
                    x, y = y, z

                if k == n:
                    return True

        return False
