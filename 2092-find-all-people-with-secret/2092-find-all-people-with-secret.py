class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda m:m[-1])
        secret_holders = {0, firstPerson}

        index = 0

        while index < len(meetings):
            graph = defaultdict(list)
            queue = deque()
            time = meetings[index][-1]

            while index < len(meetings) and meetings[index][-1] == time:
                x, y, _ = meetings[index]
                graph[x].append(y)
                graph[y].append(x)
                index += 1

            for person in graph:
                if person in secret_holders:
                    queue.append(person)

            while queue:
                p = queue.pop()
                for nei in graph[p]:
                    if nei not in secret_holders:
                        secret_holders.add(nei)
                        queue.append(nei)

        return list(secret_holders)
