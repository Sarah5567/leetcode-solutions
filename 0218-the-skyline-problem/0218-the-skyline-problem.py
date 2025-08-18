class Solution:
    def recurSkyline(
        self,
        buildings: List[List[int]],
        silhouettes: List[List[int]],
        buildingsRange: Tuple[int, int],
        coveredArea: int = 0
    ) -> None:
        if buildingsRange[0] >= buildingsRange[1]:
            return

        # Find the highest building in the current range
        highestBuildingIdx = max(
            range(buildingsRange[0], buildingsRange[1]),
            key=lambda i: buildings[i][-1]
        )
        
        l, r, h = buildings[highestBuildingIdx]
        l = max(l, coveredArea)  # avoid overlap with already covered area
        if l < r:  # only add if it's a valid segment
            silhouettes.append([l, r, h])

        # Recurse left and right
        self.recurSkyline(buildings, silhouettes, (buildingsRange[0], highestBuildingIdx), coveredArea)
        self.recurSkyline(buildings, silhouettes, (highestBuildingIdx + 1, buildingsRange[1]), r)

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        silhouettes = []
        self.recurSkyline(buildings, silhouettes, (0, len(buildings)))        
        silhouettes.sort(key=lambda s: (s[0], -s[2], s[1]))

        # Sweep line merge
        res = []
        curr_height = 0
        curr_end = 0

        points = []
        for l, r, h in silhouettes:
            points.append((l, -h))  # entering
            points.append((r, h))   # leaving
        points.sort()

        import heapq
        heap = [0]
        active = {0:1}

        prev_x, prev_h = 0, 0
        for x, h in points:
            if h < 0:  # entering
                heapq.heappush(heap, h)
            else:      # leaving
                heap.remove(-h)
                heapq.heapify(heap)

            curr_h = -heap[0]
            if curr_h != prev_h:
                res.append([x, curr_h])
                prev_h = curr_h

        return res
