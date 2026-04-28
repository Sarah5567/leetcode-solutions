class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        length = [1] * len(nums)
        parent = [-1] * len(nums)

        largest = 0

        for i, num in enumerate(nums):
            for j in range(i):
                if num % nums[j] == 0 and length[j] >= length[i]:
                    length[i] = length[j] + 1
                    parent[i] = j

                    if length[i] > length[largest]:
                        largest = i

        index = largest
        subset = []

        while index != -1:
            subset.append(nums[index])
            index = parent[index]

        return subset
