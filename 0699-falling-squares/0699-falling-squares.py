class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        highest = [0] * len(positions)
        squares = []

        for idx, (left, side_length) in enumerate(positions):
            right = left + side_length
            highest_base = 0
            for square_left, square_right, height in squares:
                if left < square_right and square_left < right:
                    highest_base = max(highest_base, height)

            cur_height = highest_base + side_length
            highest[idx] = max(cur_height, highest[idx - 1]) if idx else cur_height
            squares.append([left, left + side_length, cur_height])

        return highest