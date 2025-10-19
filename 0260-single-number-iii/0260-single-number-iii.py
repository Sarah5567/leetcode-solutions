class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitNum = 0
        while sum((num >> bitNum) & 1 for num in nums) % 2 == 0:
            bitNum += 1

        bitAt = [[0, 0], [0, 0]]
        mask, matchBits0, matchBits1, i = 0, 0, 0, 0
        
        while not (bitAt[0][0] == 1 or bitAt[0][1] == 1) or not (bitAt[1][0] == 1 or bitAt[1][1] == 1):
            bitAt = [[0, 0], [0, 0]]
            for num in nums:
                if ((num >> bitNum) & 1) == 0:
                    if (num & mask) == matchBits0:
                        bitAt[0][(num >> i) & 1] += 1
                elif (num & mask) == matchBits1:
                    bitAt[1][(num >> i) & 1] += 1

            if bitAt[0][1] % 2 == 1:
                matchBits0 |= 1 << i
            if bitAt[1][1] % 2 == 1:
                matchBits1 |= 1 << i

            mask *= 2
            mask += 1
            i += 1

        first = next(
            (num for num in nums if ((num >> bitNum) & 1) == 0 and (num & mask) == matchBits0),
            None
        )
        second = next(
            (num for num in nums if ((num >> bitNum) & 1) == 1 and (num & mask) == matchBits1),
            None
        )
        return [first, second]