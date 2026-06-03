class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        land_first = float('inf')
        for start_time, duration in zip(landStartTime, landDuration):
            land_first = min(land_first, start_time + duration)
        
        water_first = float('inf')
        water_last = float('inf')
        for start_time, duration in zip(waterStartTime, waterDuration):
            water_first = min(water_first, start_time + duration)
            water_last = min(water_last, max(start_time, land_first) + duration)

        land_last = float('inf')
        for start_time, duration in zip(landStartTime, landDuration):
            land_last = min(land_last, max(start_time, water_first) + duration)

        return min(land_last, water_last)
