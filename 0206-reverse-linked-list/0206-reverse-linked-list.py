# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = None
        b = head
        while b != None:
            tempb = b.next
            tempa = b
            b.next = a
            a = tempa
            b = tempb
        return a
        