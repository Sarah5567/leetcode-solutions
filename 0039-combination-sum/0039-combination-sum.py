class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtracking(numbers, cur_sum, index):
            if cur_sum == target:
                ans.append(numbers.copy())
                return
            if index == len(candidates):
                return

            while cur_sum <= target:
                backtracking(numbers, cur_sum, index + 1)
                cur_sum += candidates[index]
                numbers.append(candidates[index])

            while numbers and numbers[-1] == candidates[index]:
                numbers.pop()

        backtracking([], 0, 0)
        return ans
