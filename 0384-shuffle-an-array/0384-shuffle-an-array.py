class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        shuffled_arr = self.nums[:]
        n = len(shuffled_arr)

        for idx in range(n):
            new_idx = random.randint(idx, n - 1)
            shuffled_arr[idx], shuffled_arr[new_idx] = shuffled_arr[new_idx], shuffled_arr[idx]

        return shuffled_arr
