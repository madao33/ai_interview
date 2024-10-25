# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        ans = 0
        while head != None:
            nums.append(head.val)
            head = head.next
        left, right = 0, len(nums) - 1
        while left < right:
            ans = max(ans, nums[left] + nums[right])
            left += 1
            right -= 1
        return ans