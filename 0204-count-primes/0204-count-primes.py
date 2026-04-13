class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
            
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, n):
            if is_prime[i]:
                for j in range(i * 2, n, i):
                    is_prime[j] = False

        return sum(is_prime)
        