# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        elif list1.val < list2.val:
            a = list1
            b = list2
        else:
            a = list2
            b = list1
        start = a
        while a != None and b != None:
            storea = a.next
            storeb = b.next
            print(a.val, b.val)
            if storea == None and storeb == None:
                a.next = b
                break
            elif storea == None:
                a.next = b
                break
            if b.val < a.next.val:
                a.next = b
                b.next = storea
                b = storeb
            a = a.next
        
        return start
            
