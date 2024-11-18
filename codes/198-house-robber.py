from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        pre1, prev2 = nums[0], max(nums[1], nums[0])
        ans, cur = 0, 0
        for i in range(2, n):
            cur = max(pre1 + nums[i], prev2)
            ans = max(ans, cur)
            pre1, prev2 = prev2, cur
        return ans
    
print(Solution().rob([2,1,1,2]))