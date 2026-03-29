class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        change = [0] * n

        score = 0
        
        # initial score + build change array
        for i, val in enumerate(nums):
            if val <= i:
                score += 1

            low = (i + 1) % n
            high = (i - val + 1) % n

            change[low] += 1
            change[high] -= 1

            if low >= high:
                change[0] += 1

        max_score = score
        best_k = 0

        # sweep line
        for k in range(1, n):
            score += change[k]
            if score > max_score:
                max_score = score
                best_k = k

        return best_k
