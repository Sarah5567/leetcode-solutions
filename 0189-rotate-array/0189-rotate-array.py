class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        g = gcd(n, k)

        for start in range(g):
            current = start
            prev = nums[current]

            while True:
                nxt = (current + k) % n
                nums[nxt], prev = prev, nums[nxt]
                current = nxt

                if current == start:
                    break
