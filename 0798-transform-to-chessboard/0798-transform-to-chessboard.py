class Solution:
    def isValid(self, lines):
        n = len(lines)
        first = lines[0]
        inv_first = [1 - x for x in first]
        count = 0
        
        for line in lines:
            if line != first and line != inv_first:
                return False
            if line == first:
                count += 1
                
        return n // 2 <= count <= (n + 1) // 2

    def count_swaps(self, line, start_bit):
        return sum((bit != (i %2 ^ start_bit)) for i, bit in enumerate(line))
        
    def minSwaps(self, line):
        n = len(line)
        ones = sum(line)
        
        if abs( n - 2 * ones) > 1:
            return -1
            
        if n % 2 == 0:
            return min(self.count_swaps(line, 0), self.count_swaps(line, 1)) // 2
        else:
            expected_start = 1 if ones * 2 > n else 0
            return self.count_swaps(line, expected_start) // 2
                
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        rows = board
        cols = list(map(list, zip(*board)))
        
        if not self.isValid(rows) or not self.isValid(cols):
            return -1
            
        row_swap = self.minSwaps(rows[0])
        col_swaps = self.minSwaps([row[0] for row in board])
        
        if row_swap == -1 or col_swaps == -1:
            return -1
        
        return row_swap + col_swaps        