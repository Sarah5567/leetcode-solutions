class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) / 2
        costs.sort(key=lambda cost: abs(cost[0] - cost[1]))

        total_cost = 0
        people_in_a, people_in_b = 0, 0
        for a_cost, b_cost in reversed(costs):
            if (a_cost < b_cost and people_in_a < n) or people_in_b == n:
                people_in_a += 1
                total_cost += a_cost
            else:
                people_in_b += 1
                total_cost += b_cost

        return total_cost