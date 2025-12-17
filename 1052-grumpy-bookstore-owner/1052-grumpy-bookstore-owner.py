class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n : int = len(customers)
        technique_gain : int = sum(customers[i] * grumpy[i] for i in range(minutes))
        satisfied_customers : int = sum(customers[i] for i in range(minutes) if not grumpy[i])
        max_technique_gain : int = technique_gain

        for i in range(minutes, n):
            leaving_customers = i - minutes
            technique_gain -= customers[leaving_customers] * grumpy[leaving_customers]

            if grumpy[i]:
                technique_gain += customers[i]
                max_technique_gain = max(max_technique_gain, technique_gain)
            else:
                satisfied_customers += customers[i]

        return satisfied_customers + max_technique_gain
       