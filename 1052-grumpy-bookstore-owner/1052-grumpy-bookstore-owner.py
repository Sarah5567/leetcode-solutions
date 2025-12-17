class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n : int = len(customers)
        technique_gain : int = sum(customers[i] * grumpy[i] for i in range(minutes))
        satisfied_customers : int = technique_gain

        for i in range(minutes, n):
            leaving_customers = i - minutes
            technique_gain -= customers[leaving_customers] * grumpy[leaving_customers]
            technique_gain += customers[i] * grumpy[i]
            satisfied_customers = max(satisfied_customers, technique_gain)

        satisfied_customers += sum(customers[i] for i in range(n) if not grumpy[i])
        return satisfied_customers
       