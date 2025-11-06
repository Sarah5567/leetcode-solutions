class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occurrences = [-1] * (len(nums) + 1)
        index = 1

        for i in range(len(nums)):
            if nums[i] == x:
                occurrences[index] = i
                index += 1
        
        res = [-1] * len(queries)
        for i in range(len(queries)):
            if queries[i] <=  len(nums):
                res[i] = occurrences[queries[i]]

        return res
        