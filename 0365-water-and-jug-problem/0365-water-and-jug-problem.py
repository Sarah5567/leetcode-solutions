class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        return target <= x + y and target % gcd(x, y) == 0
