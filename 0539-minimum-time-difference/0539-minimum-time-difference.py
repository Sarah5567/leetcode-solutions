class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = [int(time_point[:2]) * 60 + int(time_point[3:]) for time_point in timePoints]
        times.sort()

        minimum = min((times[i] - times[i - 1] for i in range(1, len(times))))
        return min(minimum, 24 * 60 - times[-1] + times[0])
