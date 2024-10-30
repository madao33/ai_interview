class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def calcTime(piles, speed):
            sum = 0
            for pile in piles:
                sum += (pile + speed - 1) // speed
            return sum
        
        while left < right:
            mid = (left + right) // 2
            if calcTime(piles, mid) <= h:
                right = mid
            else:
                left = mid + 1
        return right

