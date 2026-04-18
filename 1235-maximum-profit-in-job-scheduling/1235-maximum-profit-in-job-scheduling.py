class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        ends = [end for start, end, prof in jobs]

        dp = [0] * n
        
        for i in range(n):
            start, end, prof = jobs[i]
            prev_job = bisect.bisect_right(ends, start) - 1
            dp[i] = max(dp[i - 1], dp[prev_job] + prof)

        return max(dp)
