class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 3:
            return False
        first, second = nums[0], float('inf')
        i = 0
        for i in range(1, N):
            num = nums[i]
            if num > second:
                return True
            if num > first:
                second = num
            else:
                first = num
        return False