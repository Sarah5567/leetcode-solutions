class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        frequencies = [[] for _ in range(len(nums) + 1)]

        for num, frequency in counts.items():
            frequencies[frequency].append(num)

        res = []
        idx = -1
        while len(res) < k:
            res += frequencies[idx]
            idx -= 1

        return res
