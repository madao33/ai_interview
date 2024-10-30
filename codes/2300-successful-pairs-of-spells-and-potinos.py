from typing import List


class Solution:

    def binarySearch(self, potions: List[int], target: int) -> int:
        left, right = -1, len(potions)
        while left + 1 < right:
            mid = (left + right) // 2
            if potions[mid] <= target:
                left = mid
            else:
                right = mid
        return right

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for spell in spells:
            target = (success - 1) / spell
            temp = self.binarySearch(potions, target)
            res.append(len(potions) - temp)
        return res 


print(Solution().successfulPairs([5,1,3], [1,2,3,4,5], 7))