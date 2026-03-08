class Solution:
    def waysToBuildRooms(self, prevRoom):
        g = defaultdict(list)
        for i in range(1, len(prevRoom)):
            g[prevRoom[i]].append(i)

        def dfs(u):
            size, ways = 1, 1
            for v in g[u]:
                s, w = dfs(v)
                ways = ways * w * comb(size + s - 1, s)
                size += s
            return size, ways

        return dfs(0)[1] % (10**9 + 7)
