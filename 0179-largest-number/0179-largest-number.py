class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = list(map(str, nums))

        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        strs.sort(key=cmp_to_key(compare))

        result = ''.join(strs)

        return '0' if result[0] == '0' else result
