class MyCalendarThree:

    def __init__(self):
        self.k = 0
        self.n = 0
        self.start = []
        self.end = []

    def book(self, startTime: int, endTime: int) -> int:
        bookings = 1
        startIdx = bisect.bisect_left(self.start, startTime)
        endIdx = bisect.bisect_right(self.end, startTime)   # ← תיקון כאן

        for i in range(startIdx):
            if self.end[i] > startTime:
                bookings += 1

        self.k = max(self.k, bookings)

        indexInStart, indexInEnd = startIdx, endIdx
        while (indexInStart < self.n and self.start[indexInStart] < endTime) or \
              (indexInEnd < self.n and self.end[indexInEnd] < endTime):

            if indexInStart < self.n and (indexInEnd == self.n or self.start[indexInStart] < self.end[indexInEnd]):
                indexInStart += 1
                bookings += 1
                self.k = max(self.k, bookings)
            else:
                indexInEnd += 1
                bookings -= 1

        bisect.insort(self.start, startTime)
        bisect.insort(self.end, endTime)
        self.n += 1
        return self.k
