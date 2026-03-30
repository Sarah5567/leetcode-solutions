class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        lamps_set =  {(x, y) for x, y in lamps}

        rows = defaultdict(int)
        cols = defaultdict(int)
        diag1 = defaultdict(int)
        diag2 = defaultdict(int)

        for r, c in lamps_set:
            rows[r] += 1
            cols[c] += 1
            diag1[r - c] += 1
            diag2[r + c] += 1

        ans = [0] * len(queries)

        for i, (r, c) in enumerate(queries):
            if rows[r] or cols[c] or diag1[r - c] or diag2[r + c]:
                ans[i] = 1
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx = r + dx
                        ny = c + dy

                        if (nx, ny) in lamps_set:
                            lamps_set.remove((nx, ny))

                            rows[nx] -= 1
                            cols[ny] -= 1
                            diag1[nx - ny] -= 1
                            diag2[nx + ny] -= 1

        return ans