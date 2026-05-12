class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t:t[1] - t[0], reverse=True)

        initial_amount = 0
        cur_amount = 0

        for actual, minimum in tasks:
            if minimum > cur_amount:
                initial_amount += minimum - cur_amount
                cur_amount = minimum

            cur_amount -= actual

        return initial_amount
