# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.next_element = self.iterator.next() if self.iterator.hasNext() else None       

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_element
        

    def next(self):
        """
        :rtype: int
        """
        curr = self.next_element
        self.next_element = self.iterator.next() if self.iterator.hasNext() else None
        return curr

        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_element != None
        