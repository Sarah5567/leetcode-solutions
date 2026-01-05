class Solution:

    def __init__(self, w: List[int]):
        self.prefix = list(accumulate(w))

    def pickIndex(self) -> int:
        pick = random.randint(1, self.prefix[-1])
        return bisect.bisect_left(self.prefix, pick)
