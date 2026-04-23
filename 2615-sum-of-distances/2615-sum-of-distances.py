class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indexes = {}

        for i, num in enumerate(nums):
            if num not in indexes:
                indexes[num] = []
            indexes[num].append(i)

        arr = [0] * len(nums)

        for indexes_arr in indexes.values():
            right_sum = sum(indexes_arr)
            left_sum = 0
            n = len(indexes_arr)

            for i, idx in enumerate(indexes_arr):
                right_sum -= idx
                arr[idx] = right_sum - (idx * (n - i - 1)) + (idx * i) - left_sum
                left_sum += idx
                
        return arr
