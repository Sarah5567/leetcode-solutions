class Solution:
    def count_ones_upto(self, n, bit):
        cycle = 1 << (bit + 1)
        full_cycles = (n + 1) // cycle
        remainder = (n + 1) % cycle
        return full_cycles * (cycle >> 1) + max(0, remainder - (cycle >> 1))

    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        duplicate = 0

        count_ones_upto = self.count_ones_upto
        max_bits = max(nums).bit_length()

        for bit in range(max_bits):
            ones = sum((num >> bit) & 1 for num in nums)
            expected_ones = count_ones_upto(n, bit)

            if ones > expected_ones:
                duplicate |= (1 << bit)

        return duplicate
