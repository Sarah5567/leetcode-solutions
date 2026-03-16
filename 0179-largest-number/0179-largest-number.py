class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            if str(a) + str(b) > str(b) + str(a):
                return -1
            if str(a) + str(b) < str(b) + str(a):
                return 1
            return 0

        nums = sorted(nums, key=cmp_to_key(compare))
        result = ''.join(map(str, nums))
        return '0' if result[0] == '0' else result