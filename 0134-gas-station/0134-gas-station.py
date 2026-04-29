class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start_point = 0
        gas_amount = 0
        required_to_begin = 0

        for i in range(n):
            gas_amount += gas[i] - cost[i]
            if gas_amount < 0:
                required_to_begin += abs(gas_amount)
                gas_amount = 0
                start_point = i + 1

        return start_point if gas_amount >= required_to_begin else -1
