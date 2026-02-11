class AllOne:

    class Bucket:
        def __init__(self, count):
            self.count = count
            self.keys = set()
            self.prev = None
            self.next = None

    def __init__(self):
        self.k2bucket = {}

        self.head = self.Bucket(0)
        self.tail = self.Bucket(0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert_after(self, node, new_node):
        nxt = node.next
        new_node.prev = node
        new_node.next = nxt
        node.next = new_node
        nxt.prev = new_node

    def _insert_before(self, node, new_node):
        prv = node.prev
        new_node.next = node
        new_node.prev = prv
        prv.next = new_node
        node.prev = new_node

    def _remove_bucket_if_empty(self, node):
        if node is self.head or node is self.tail:
            return
        if node.keys:
            return
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.k2bucket:
            first = self.head.next
            if first is self.tail or first.count != 1:
                new_bucket = self.Bucket(1)
                self._insert_after(self.head, new_bucket)
                first = new_bucket
            first.keys.add(key)
            self.k2bucket[key] = first
            return

        curr = self.k2bucket[key]
        nxt = curr.next
        new_count = curr.count + 1

        if nxt is self.tail or nxt.count != new_count:
            new_bucket = self.Bucket(new_count)
            self._insert_after(curr, new_bucket)
            nxt = new_bucket

        curr.keys.remove(key)
        nxt.keys.add(key)
        self.k2bucket[key] = nxt

        self._remove_bucket_if_empty(curr)

    def dec(self, key: str) -> None:
        curr = self.k2bucket[key]
        new_count = curr.count - 1

        if new_count == 0:
            curr.keys.remove(key)
            del self.k2bucket[key]
            self._remove_bucket_if_empty(curr)
            return

        prv = curr.prev
        if prv is self.head or prv.count != new_count:
            new_bucket = self.Bucket(new_count)
            self._insert_before(curr, new_bucket)
            prv = new_bucket

        curr.keys.remove(key)
        prv.keys.add(key)
        self.k2bucket[key] = prv

        self._remove_bucket_if_empty(curr)

    def getMaxKey(self) -> str:
        if self.tail.prev is self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next is self.tail:
            return ""
        return next(iter(self.head.next.keys))
