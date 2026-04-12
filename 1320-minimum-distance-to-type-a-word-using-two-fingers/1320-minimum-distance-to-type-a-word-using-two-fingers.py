class Solution:
    def minimumDistance(self, word: str) -> int:
        def idx(c):
            return ord(c) - ord('A')
        
        def dist(a, b):
            if a == -1:
                return 0
            x1, y1 = divmod(a, 6)
            x2, y2 = divmod(b, 6)
            return abs(x1 - x2) + abs(y1 - y2)
        
        dp = [float('inf')] * 26
        
        prev = idx(word[0])
        
        for c in range(26):
            dp[c] = 0
        
        for i in range(1, len(word)):
            curr = idx(word[i])
            new_dp = [float('inf')] * 26
            
            for c in range(26):
                new_dp[c] = min(new_dp[c], dp[c] + dist(prev, curr))
                
                new_dp[prev] = min(new_dp[prev], dp[c] + dist(c, curr))
            
            dp = new_dp
            prev = curr
        
        return min(dp)