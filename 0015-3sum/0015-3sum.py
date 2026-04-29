class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        seen_values = Counter(nums)
        
        sorted_vals = sorted(seen_values.keys())
        seen_pairs = defaultdict(list)
        answer = []

        for i, val in enumerate(sorted_vals):
            for n1, n2 in seen_pairs[-val]:
                answer.append((n1, n2, val))

            val_count = seen_values[val]
            
            if val_count > 1:
                target = -val * 2
                if target in seen_values and (val_count > 2 or val != 0):
                    answer.append((val, val, target))

            for j in range(i):
                seen_pairs[val + sorted_vals[j]].append((val, sorted_vals[j]))

        return answer