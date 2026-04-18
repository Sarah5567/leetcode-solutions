class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        person1 = -1
        max_distance = 0

        while person1 < n:
            person2 = person1
            person1 += 1
            while person1 < n and not seats[person1]:
                person1 += 1

            if person2 == -1:
                max_distance = person1
            elif person1 == n:
                max_distance = max(max_distance, n - person2 - 1)
            else:
                max_distance = max(max_distance, (person1 - person2) // 2)

        return max_distance
