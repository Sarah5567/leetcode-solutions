class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        MOD = 1000000007

        n = len(conversions) + 1
        directConversions : List[List[int]] = [[] for _ in range(n)]
        for i, conversion in enumerate(conversions):
            directConversions[conversion[0]].append((conversion[1], conversion[2]))

        equivalents : List[int] = [1] * n
        q = deque()

        q.append(0)
        while q:
            sourceUnit = q.popleft()
            for targetUnit, conversionFactor in directConversions[sourceUnit]:
                equivalents[targetUnit] = (equivalents[sourceUnit] * conversionFactor) % MOD
                q.append(targetUnit)

        return equivalents

