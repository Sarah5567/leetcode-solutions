class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        correct_idx = 1
        freq = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                freq = 0
            
            freq += 1

            if freq <= 2:
                nums[correct_idx] = nums[i]
                correct_idx += 1

        return correct_idx
