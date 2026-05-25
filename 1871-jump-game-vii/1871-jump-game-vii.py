class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False

        n = len(s)
        intervals = deque()
        intervals.append([0, 0])
        farthest = 0

        while intervals and intervals[0][0] < n:
            l, r = intervals.popleft()

            for i in range(max(l, farthest), min(r + 1, n)):
                if s[i] == '1':
                    continue

                if not intervals or i + minJump > intervals[-1][1]:
                    intervals.append([i + minJump, i + maxJump])
                else:
                    intervals[-1][1] = i + maxJump

                if i + minJump <= n - 1 <= i + maxJump:
                    return True

            farthest = r

        return False
