class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        res = []

        def dfs(node):
            while graph[node]:
                nxt = heapq.heappop(graph[node])
                dfs(nxt)
            res.append(node)

        dfs("JFK")
        return res[::-1]
