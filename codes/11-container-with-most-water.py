from typing import List


class Solution:

    def getArea(self, height: List[int], left: int, right: int) -> int:
        return min(height[left], height[right]) * (right - left)
    
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        left, right = 0, N-1
        res = self.getArea(height, left, right)
        while left < right:
            if height[left] < height[right]:
                left += 1
                res = max(self.getArea(height, left, right), res)
            else:
                right -= 1
                res = max(self.getArea(height, left, right), res)
        return res


print(Solution().maxArea([2,3,4,5,18,17,6]))