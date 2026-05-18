class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(reverse=True, key=lambda p:p[0])
        stack = []

        count = 0
        max_defense_level = 0
        prev_defense_level = 0

        for i, (attack, defense) in enumerate(properties):
            if i > 0 and attack < properties[i - 1][0]:
                prev_defense_level = max_defense_level

            if defense > max_defense_level:
                max_defense_level = defense

            if defense < prev_defense_level:
                count += 1

        return count