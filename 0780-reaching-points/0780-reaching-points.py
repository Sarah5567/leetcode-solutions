class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx

        if tx == sx and ty == sy:
            return True

        if tx == sx and ty > sy:
            return (ty - sy) % sx == 0

        if ty == sy and tx > sx:
            return (tx - sx) % sy == 0

        return False