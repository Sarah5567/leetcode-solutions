class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        count_visited = 0

        def dfs(room: int) -> True:
            visited[room] = True
            
            nonlocal count_visited
            count_visited += 1
            if count_visited == n:
                return True

            for key in rooms[room]:
                if not visited[key]:
                    if dfs(key):
                        return True

            return False

        return dfs(0)