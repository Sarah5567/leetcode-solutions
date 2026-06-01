class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 1000000007
        seen = defaultdict(int)
        need = defaultdict(int)

        meals = 0

        for d in deliciousness:
            if d == 0:
                meals = (meals + need[0]) % MOD
                seen[0] += 1
            else:
                closest_pow = 1 << (d - 1).bit_length()
                meals = (meals + seen[closest_pow - d] + need[d]) % MOD
                
                seen[d] += 1
                need[closest_pow - d] += 1
                if d == closest_pow:
                    need[d] += 1

        return meals
