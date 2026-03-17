class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.pos = defaultdict(set)

    def insert(self, val: int) -> bool:
        exists = len(self.pos[val]) > 0

        self.arr.append(val)
        self.pos[val].add(len(self.arr) - 1)

        return not exists

    def remove(self, val: int) -> bool:
        if not self.pos[val]:
            return False

        remove_idx = self.pos[val].pop()
        last_val = self.arr[-1]

        self.arr[remove_idx] = last_val

        self.pos[last_val].add(remove_idx)
        self.pos[last_val].discard(len(self.arr) - 1)

        self.arr.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
