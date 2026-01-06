class Solution:

    def canReorderDoubled(self, arr: List[int]) -> bool:
        uniqe_elements = sorted(list(set(arr)))
        count_values = Counter(arr)
        zero_index = bisect_left(uniqe_elements, 0)

        def checkDoublePairs(begin, steps):
            for num in uniqe_elements[begin::steps]:
                if count_values[num] > 0:
                    if num * 2 in count_values and count_values[num * 2] >= count_values[num]:
                        count_values[num * 2] -= count_values[num]
                    else:
                        return False
            return True

        return checkDoublePairs(begin=zero_index, steps=1) and (not zero_index or checkDoublePairs(begin=zero_index-1, steps=-1))
