class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        times = [(g, p) for g, p in zip(growTime, plantTime)]
        times.sort(reverse=True)

        plant_end = 0
        grow_end = 0

        for grow, plant in times:
            plant_end += plant
            grow_end = max(grow_end, plant_end + grow)

        return grow_end
