class Solution:
    def waysToBuildRooms(self, prevRoom):
        MOD = 10**9 + 7
        n = len(prevRoom)

        g = defaultdict(list)
        for i in range(1, n):
            g[prevRoom[i]].append(i)

        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        # fast combination
        def comb(n, k):
            return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

        def dfs(u):
            size = 1
            ways = 1

            for v in g[u]:
                s, w = dfs(v)

                # combine permutations
                ways = ways * w % MOD
                ways = ways * comb(size + s - 1, s) % MOD

                size += s

            return size, ways

        return dfs(0)[1]
