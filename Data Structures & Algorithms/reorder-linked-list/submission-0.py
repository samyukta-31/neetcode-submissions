# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fp = head
        sp = head

        # finding mid point
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        
        second = sp.next 
        sp.next = None # first split from second
        
        # reversing second linked list
        prev = None
        scurr = second
        while scurr:
            nxt = scurr.next
            scurr.next = prev
            prev = scurr
            scurr = nxt

        # combining both in place
        fcurr = head
        scurr = prev
        while fcurr and scurr:
            fnext = fcurr.next
            snext = scurr.next
            fcurr.next = scurr
            scurr.next = fnext

            fcurr = fnext
            scurr = snext
        
            
            


