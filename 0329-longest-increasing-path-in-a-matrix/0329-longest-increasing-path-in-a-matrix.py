class Solution:

    def buildGraph(self, matrix: List[List[int]]) -> Dict[Tuple[int, int], List[Tuple[int, int]]]:
    
        graph = {}
        
        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                neighbors = []
                if i > 0 and matrix[i - 1][j] > n:
                    neighbors.append((i - 1, j))
                if j > 0 and matrix[i][j - 1] > n:
                    neighbors.append((i, j - 1))
                if i < len(matrix) - 1 and matrix[i + 1][j] > n:
                    neighbors.append((i + 1, j))
                if j < len(row) - 1 and matrix[i][j + 1] > n:
                    neighbors.append((i, j + 1))
                graph[(i, j)] = neighbors
        
        return graph
             
             
    def dfs(self, graph : Dict[Tuple[int, int], List[Tuple[int, int]]], longestPathes : List[List[int]], u : Tuple[int, int]) -> int:
        i, j = u
        
        max_len = 1
        for ni, nj in graph[u]:
            if longestPathes[ni][nj] == 0:
                self.dfs(graph, longestPathes, (ni, nj))
            path_len = 1 + longestPathes[ni][nj]
            max_len = max(max_len, path_len)
        
        longestPathes[i][j] = max_len
        return max_len

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        graph = self.buildGraph(matrix)
        longestPathes = [[0] * n for _ in range(m)]
        
        maxPath = 0
        for i in range(m):
            for j in range(n):
                if longestPathes[i][j] == 0:
                    self.dfs(graph, longestPathes, (i, j))
                maxPath = max(maxPath, longestPathes[i][j])
        
        return maxPath