class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)
        sorted_values = sorted(counts.keys())

        q = deque()
        Pending = namedtuple("Pending", ["idx", "amount"])
        cards_in_q = 0

        for i, val in enumerate(sorted_values):
            if q and q[0].idx + groupSize == i:
                cards_in_q -= q[0].amount
                q.popleft()

            if cards_in_q > 0 and val != sorted_values[i - 1] + 1:
                return False
            
            freq = counts[val]

            if freq < cards_in_q:
                return False

            elif freq > cards_in_q:
                new_groups = freq - cards_in_q
                q.append(Pending(i, new_groups))
                cards_in_q += new_groups

        if q and q[0].idx + groupSize == len(sorted_values):
            cards_in_q -= q[0].amount
            q.popleft()

        return cards_in_q == 0
