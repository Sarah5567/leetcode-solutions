class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        left = 0
        right = m - 1

        while left < right:
            mid = left + (right - left) // 2

            if matrix[mid][-1] > target:
                right = mid
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:
                left = right = mid

        mid = left + (right - left) // 2
        index = bisect.bisect_left(matrix[mid], target)

        return index < len(matrix[mid]) and matrix[mid][index] == target
