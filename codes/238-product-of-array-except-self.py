

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prev, back = [1 for i in range(N+1)], [1 for i in range(N+1)]
        for i in range(N):
            prev[i+1] = prev[i] * nums[i]
            back[N-i-1] = back[N-i] * nums[N-i-1]
        res = [prev[i] * back[i+1] for i in range(N)]
        return res



sol = Solution().productExceptSelf([1,2,3,4])
print(sol)