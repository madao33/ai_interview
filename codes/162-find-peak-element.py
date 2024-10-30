class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        def get(i: int) -> int:
            if i < 0 or i > n - 1:
                return float('-inf')
            return nums[i]
        
        left, right, ans = 0, n-1, -1
        while left <= right:
            mid = (left + right) // 2
            if get(mid - 1) < get(mid) > get(mid + 1):
                ans = mid
                break
            elif get(mid - 1) < get(mid):
                left = mid + 1
            else:
                right = mid - 1
            
        return ans
