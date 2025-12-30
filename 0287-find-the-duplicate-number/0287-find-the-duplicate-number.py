class Solution:
    def count_ones_upto(self, n, bit):
        cycle = 1 << (bit + 1)
        full_cycles = (n + 1) // cycle
        remainder = (n + 1) % cycle
        return full_cycles * (cycle >> 1) + max(0, remainder - (cycle >> 1))

    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        duplicate = 0
        max_element = max(nums)

        for bit in range(32):
            if max_element == 0:
                break

            ones = 0
            for num in nums:
                ones += (num >> bit) & 1

            expected_ones = self.count_ones_upto(n, bit)

            if ones > expected_ones:
                duplicate |= (1 << bit)

            max_element >>= 1

        return duplicate
