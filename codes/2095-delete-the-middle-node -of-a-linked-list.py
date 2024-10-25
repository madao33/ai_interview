# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        slow, fast = head, head.next
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head



print(Solution().deleteMiddle())