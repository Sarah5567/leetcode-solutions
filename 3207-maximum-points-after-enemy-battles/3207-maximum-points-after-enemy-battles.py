class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        min_val = min(enemyEnergies)
        if min_val > currentEnergy:
            return 0
            
        total = sum(enemyEnergies) - min_val + currentEnergy
        return total // min_val
        