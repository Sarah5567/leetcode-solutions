class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()

        def insert_to_queue(idx: int):
            num = nums[idx]
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(idx)

        res = [0] * (len(nums) - k + 1)
        for i in range(len(nums)):
            insert_to_queue(i)
            if i >= k - 1:
                res[i - k + 1] = nums[queue[0]]
                if queue[0] <= i + 1 - k:
                    queue.popleft()
        
        return res

