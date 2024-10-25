# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        evenHead = head.next
        oddPtr, evenPtr = head, head.next
        while evenPtr.next != None and evenPtr.next.next != None and oddPtr.next != None and oddPtr.next.next != None:
            oddPtr.next = oddPtr.next.next
            oddPtr = oddPtr.next
            evenPtr.next = evenPtr.next.next
            evenPtr = evenPtr.next
            
        if oddPtr.next != None and oddPtr.next.next != None:
            oddPtr.next = oddPtr.next.next
            oddPtr = oddPtr.next
        evenPtr.next = None
        oddPtr.next = evenHead
        return head
        