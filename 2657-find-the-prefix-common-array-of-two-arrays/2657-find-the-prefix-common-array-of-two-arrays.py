class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)

        C = [0] * n

        for i in range(n):
            a = abs(A[i])
            b = abs(B[i])

            A[a - 1] = -A[a - 1]
            B[b - 1] = -B[b - 1]

            C[i] = C[i - 1] if i else 0

            if B[a - 1] < 0:
                C[i] += 1
            if A[b - 1] < 0 and a != b:
                C[i] += 1

        return C
        