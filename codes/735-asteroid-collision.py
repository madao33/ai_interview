from typing import List


class Solution:

    def collide(self, aster1: int, aster2: int) -> bool:
        if aster1 > 0 and aster2 < 0:
            return True
        return False

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for aster in asteroids:
            alive = True
            while len(res) > 0 and self.collide(res[-1], aster):
                if abs(res[-1]) < abs(aster):
                    res.pop()
                elif abs(res[-1]) == abs(aster):
                    res.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break
            if alive:
                res.append(aster)
        return res


print(Solution().asteroidCollision([5,10,-5]))