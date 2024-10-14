class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        z_ptr = 0
        for i in range(N):
            if nums[i] != 0:
                nums[z_ptr] = nums[i]
                z_ptr += 1
        for j in range(z_ptr, N):
            nums[j] = 0
            