class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])

        elif len(nums) == 2:
            return f'{str(nums[0])}/{str(nums[1])}'

        else:
            middle = '/'.join(map(str, nums[1:]))
            return f'{str(nums[0])}/({middle})'
