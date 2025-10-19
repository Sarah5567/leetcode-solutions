class Solution:
    def findOneNumber(self, nums: List[int], bitNum: int, identifier: int):
        bitAt = [0, 0]
        mask, matchBits, i = 0, 0, 0
        
        while not (bitAt[0] == 1 or bitAt[1] == 1):
            bitAt = [0, 0]
            for num in nums:
                if ((num >> bitNum) & 1) == identifier and (num & mask) == matchBits:
                    bitAt[(num >> i) & 1] += 1

            if bitAt[1] % 2 == 1:
                matchBits |= 1 << i
            mask *= 2
            mask += 1
            i += 1

        return next(
            (num for num in nums if ((num >> bitNum) & 1) == identifier and (num & mask) == matchBits),
            None
        )

    def singleNumber(self, nums: List[int]) -> List[int]:
        bitNum = 0
        while sum((num >> bitNum) & 1 for num in nums) % 2 == 0:
            bitNum += 1

        return [self.findOneNumber(nums, bitNum, 0), self.findOneNumber(nums, bitNum, 1)]