class Solution:
    def get_left_zeros(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        left_zeros = [[0] * n for _ in range(m)]

        for i in range(m):
            left_zeros[i][0] = grid[i][0] ^ 1

        for i in range(m):
            for j in range(1, n):
                left_zeros[i][j] = (left_zeros[i][j-1] + 1) * (not grid[i][j])

        return left_zeros

    def insert_to_stack(self, stack: deque, left_zeros: List[List[int]], col: int, i: int) -> None:
        while len(stack) > 0 and left_zeros[stack[-1]][col] >= left_zeros[i][col]:
            stack.pop()
        stack.append(i)
    
    def fill_last_stamps_col(self, stamps: List[List[bool]], stampHeight: int) -> None:
        m, n = len(stamps), len(stamps[0])

        for j in range(n):
            last_start = m * stampHeight
            for i in range(m - 1, -1, -1):
                if stamps[i][j]:
                    last_start = i
                elif last_start - i < stampHeight:
                    stamps[i][j] = True

    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        left_zeros = self.get_left_zeros(grid)

        stack = deque()
        height_zeros = 0
        stamps = [[False] * n for _ in range(m)]
        for j in range(stampWidth - 1, n):
            for i in range(m):
                self.insert_to_stack(stack, left_zeros, j, i)
                height_zeros = (height_zeros + 1) * (grid[i][j] ^ 1)
                if height_zeros < stampHeight:
                    continue

                while stack[0] <= i - stampHeight:
                    stack.popleft()
                if left_zeros[stack[0]][j] >= stampWidth:
                    stamps[i][j] = True

            height_zeros = 0
            stack = deque()
        
        self.fill_last_stamps_col(stamps, stampHeight)

        for i in range(m):
            last_start = n * stampWidth
            for j in range(n - 1, -1, -1):
                if stamps[i][j]:
                    last_start = j
                elif last_start - j >= stampWidth and not grid[i][j]:
                    return False
        
        return True
