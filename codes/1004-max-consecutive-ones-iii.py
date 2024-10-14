class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lsum, rsum = 0, 0
        ans = 0
        N = len(nums)
        left = 0
        for right in range(N):
            rsum += 1 - nums[right]
            while rsum - lsum > k:
                lsum += 1 - nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
