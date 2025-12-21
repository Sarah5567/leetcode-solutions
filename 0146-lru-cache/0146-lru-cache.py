class Node:
    def __init__(self, val : int) -> None:
        self.val = val
        self.prev = None
        self.next = None

class List:
    def __init__(self) -> None:
        self._head : Node = None
        self._tail : Node = None
        self.length = 0

    def move_to_front(self, node : Node) -> None:
        if node is self._head:
            return

        if node is self._tail:
            self._tail = self._tail.prev
            self._tail.next = None
        else:
            node.next.prev = node.prev
        
        node.prev.next = node.next
        node.prev = None
        node.next = self._head
        self._head.prev = node
        self._head = node
    
    def append(self, val : int) -> Node:
        node = Node(val)
        node.next = self._head

        if self.length == 0:
            self._tail = node
        else:
            self._head.prev = node

        self._head = node

        self.length += 1
        return self._head

    def pop(self) -> int:
        tail = self._tail
        tail_val = tail.val

        if tail.prev:
            self._tail = tail.prev
            self._tail.next = None
        else:
            self._head = None
            self._tail = None

        self.length -= 1
        return tail_val



class LRUCache:

    def __init__(self, capacity: int):
        self._cache = {}
        self._recency = List()
        self._capacity = capacity

    def get(self, key: int) -> int:
        if key in self._cache:
            val, node = self._cache[key]
            self._recency.move_to_front(node)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            old_val, node = self._cache[key]
            self._cache[key] = (value, node)
            self._recency.move_to_front(node)
            return

        if self._recency.length == self._capacity:
            key_to_remove = self._recency.pop()
            del self._cache[key_to_remove]
        node = self._recency.append(key)
        self._cache[key] = (value, node)
        