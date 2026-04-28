class RandomizedSet:

    def __init__(self):
        self.val_to_idx = {}
        self.values = []
        self.capacity = 0

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False

        else:
            if self.capacity == len(self.values):
                self.values.append(val)
            else:
                self.values[self.capacity] = val

            self.val_to_idx[val] = self.capacity
            self.capacity += 1

            return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False

        else:
            self.capacity -= 1
            idx = self.val_to_idx[val]
            del self.val_to_idx[val]

            if idx < self.capacity:
                self.values[idx] = self.values[self.capacity]
                self.val_to_idx[self.values[self.capacity]] = idx

            return True

    def getRandom(self) -> int:
        random_idx = random.randrange(self.capacity)
        return self.values[random_idx]
