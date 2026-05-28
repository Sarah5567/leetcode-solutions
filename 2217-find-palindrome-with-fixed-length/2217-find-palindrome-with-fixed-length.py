class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        base = int(math.pow(10, math.ceil(intLength / 2) - 1))
        max_query = base * 9

        ans = [-1] * len(queries)

        for i, query in enumerate(queries):
            if query <= max_query:
                first_part = str(base + query - 1)
                if intLength % 2 == 1:
                    second_part = first_part[:-1][::-1]
                else:
                    second_part = first_part[::-1]
                    
                ans[i] = int(first_part + second_part)

        return ans