class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        counter1, counter2 = Counter(nums1), Counter(nums2)
        values = set(counter1.keys() | counter2.keys())
        if any((counter1[value] + counter2[value]) % 2 for value in values):
            return -1
        return sum(abs(counter1[value] - counter2[value]) // 2 for value in values) //2
