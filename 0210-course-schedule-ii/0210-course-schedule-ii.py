class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        ans = []
        visited = [False] * numCourses
        in_process = [False] * numCourses

        def dfs(course):
            visited[course] = True
            in_process[course] = True

            for next_course in graph[course]:
                if in_process[next_course]:
                    return False
                if not visited[next_course] and not dfs(next_course):
                    return False
            
            ans.append(course)
            in_process[course] = False
            return True

        for course in range(numCourses):
            if not visited[course] and not dfs(course):
                return []

        return ans
