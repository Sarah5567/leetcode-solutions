class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        numCandies = [1] * n
        
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                numCandies[i] = numCandies[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                numCandies[i] = max(numCandies[i], numCandies[i + 1] + 1)
                
        return sum(numCandies)