class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        r = bisect.bisect_left(arr, x)
        l = r - 1

        while r - l <= k:
            if l >= 0 and (r == len(arr) or abs(arr[l] - x) <= abs(arr[r] - x)):
                l -= 1
            else:
                r += 1

        return arr[l+1:r]
