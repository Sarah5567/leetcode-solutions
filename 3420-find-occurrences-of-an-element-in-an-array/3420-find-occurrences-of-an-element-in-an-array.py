class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        ith_occurrence = {}
        count = 0

        for i, num in enumerate(nums):
            if num == x:
                count += 1
                ith_occurrence[count] = i
        
        return [ith_occurrence.get(q, -1) for q in queries]
