class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        ithOccurrence = {}
        index = 1

        for i in range(len(nums)):
            if nums[i] == x:
                ithOccurrence[index] = i
                index += 1
        
        res = [-1] * len(queries)
        for i in range(len(queries)):
            if queries[i] in ithOccurrence:
                res[i] = ithOccurrence[queries[i]]

        return res
        