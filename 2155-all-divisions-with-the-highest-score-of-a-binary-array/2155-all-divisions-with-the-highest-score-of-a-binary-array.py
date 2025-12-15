class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        division_score = sum(nums)

        highest_score = division_score
        for num in nums:
            if num:
                division_score -= 1
            else:
                division_score += 1
                highest_score = max(highest_score, division_score)
        
        res = []

        division_score = sum(nums)
        if division_score == highest_score:
            res.append(0)
        for i, num in enumerate(nums):
            if num:
                division_score -= 1
            else:
                division_score += 1
                if division_score == highest_score:
                    res.append(i + 1)

        return res

