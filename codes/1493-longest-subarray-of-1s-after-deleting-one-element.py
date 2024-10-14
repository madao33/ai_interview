class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        if sum(nums) == N:
            return N - 1
        lsum, rsum = 0, 0
        left, ans = 0, 0
        for right in range(N):
            rsum += 1 - nums[right]
            while rsum - lsum > 1:
                lsum += 1 - nums[left]
                left += 1
            ans = max(ans, right - left + 1 - rsum + lsum)
        return ans