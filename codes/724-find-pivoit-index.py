from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        lsum, rsum = [0 for i in range(N+1)], [0 for i in range(N+1)]
        for i in range(N):
            lsum[i+1] += lsum[i] + nums[i]
            rsum[N-i-1] = rsum[N-i] + nums[N-i-1]

        for i in range(N):
            if lsum[i] == rsum[i+1]:
                return i
        return -1


print(Solution().pivotIndex([2,1,-1]))