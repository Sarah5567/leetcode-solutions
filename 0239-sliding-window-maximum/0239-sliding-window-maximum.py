class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        queue = deque()
        res = [0] * (n - k + 1)

        for i in range(n):
            num = nums[i]

            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)

            if queue[0] <= i - k:
                queue.popleft()

            if i >= k - 1:
                res[i - k + 1] = nums[queue[0]]

        return res
