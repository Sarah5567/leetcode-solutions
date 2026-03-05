class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        r, l = k, k
        max_score, cur_min = nums[k], nums[k]

        while l > 0 or r < len(nums) - 1:
            if l == 0 or (r < len(nums) - 1 and nums[r + 1] > nums[l - 1]):
                r += 1
                cur_min = min(cur_min, nums[r])
            else:
                l -= 1
                cur_min = min(cur_min, nums[l])
            max_score = max(max_score, cur_min * (r - l + 1))

        return max_score
