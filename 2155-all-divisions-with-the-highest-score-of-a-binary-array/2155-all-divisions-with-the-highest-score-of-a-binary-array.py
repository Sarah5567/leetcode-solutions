class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        division_score = sum(nums)
        res = [0]

        highest_score = division_score
        for i, num in enumerate(nums):
            if num:
                division_score -= 1
            else:
                division_score += 1
                if division_score == highest_score:
                    res.append(i + 1)
                elif division_score > highest_score:
                    highest_score = division_score
                    res = [i + 1]

        return res

