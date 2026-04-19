class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])

        second_last, last = -1, -1
        length = 0

        for start, end in intervals:
            if second_last < start:
                length += 1
                if last < start:
                    last, second_last = end, end - 1
                    length += 1
                elif last == end:
                    second_last = end - 1
                else:
                    last, second_last = end, last
            
        return length
