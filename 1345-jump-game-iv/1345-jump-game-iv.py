class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        values = defaultdict(list)
        for i, num in enumerate(arr):
            values[num].append(i)

        steps = [-1] * n
        q = deque()

        q.append(0)
        steps[0] = 0

        while steps[-1] == -1:
            index = q.popleft()

            for next_idx in values[arr[index]]:
                if steps[next_idx] == -1:
                    steps[next_idx] = steps[index] + 1
                    q.append(next_idx)

            del values[arr[index]]

            if index > 0 and steps[index - 1] == -1:
                steps[index - 1] = steps[index] + 1
                q.append(index - 1)
            if index < n - 1 and steps[index + 1] == -1:
                steps[index + 1] = steps[index] + 1
                q.append(index + 1)

        return steps[-1]
