class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        cur_mass = mass

        for asteroid in asteroids:
            if asteroid > cur_mass:
                return False
            cur_mass += asteroid

        return True