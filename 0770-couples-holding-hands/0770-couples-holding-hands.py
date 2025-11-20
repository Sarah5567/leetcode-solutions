class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        positions = [0] * len(row)

        # record where each person sits
        for i, person in enumerate(row):
            positions[person] = i

        swaps = 0

        # go pair by pair
        for i in range(0, len(row), 2):
            first = row[i]

            # find the expected partner
            partner = first ^ 1    # flips last bit: 0↔1, 2↔3, 4↔5...

            # already sitting together
            if row[i + 1] == partner:
                continue

            # we need to bring the partner into position i+1
            partner_pos = positions[partner]

            # swap row[i+1] with the partner
            row[i + 1], row[partner_pos] = row[partner_pos], row[i + 1]
            swaps += 1

            # update positions because we swapped
            positions[row[partner_pos]] = partner_pos
            positions[row[i + 1]] = i + 1

        return swaps
    