class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend].append((divisor, value))
            graph[divisor].append((dividend, 1/value))

        answers = [-1] * len(queries)

        def dfs(cur_dividend, divisor, answer):
            if not cur_dividend in graph or visited[cur_dividend]:
                return -1
            visited[cur_dividend] = True
                
            if cur_dividend == divisor:
                return answer

            for cur_divisor, val in graph[cur_dividend]:
                cur_answer = dfs(cur_divisor, divisor, answer * val)
                if cur_answer != -1:
                    return cur_answer

            return -1

        for i, (dividend, divisor) in enumerate(queries):
            visited = {dividend : False for dividend in graph.keys()}

            if divisor in graph:
                answers[i] = dfs(dividend, divisor, 1)

        return answers
        