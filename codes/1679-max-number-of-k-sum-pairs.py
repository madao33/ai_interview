class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        list.sort(nums)
        N = len(nums)
        left, right = 0, N - 1
        res = 0
        while left < right:
            if nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                res += 1
                left += 1
                right -= 1
        return res
