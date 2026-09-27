# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr1 = l1
        curr2 = l2
        suml = ListNode(None)
        currsum = suml
        while curr1 or curr2 or carry:
            currsum.next = ListNode(None)
            currsum = currsum.next
            s = carry
            s += curr1.val if curr1 else 0
            s += curr2.val if curr2 else 0
            carry = s // 10
            add = s % 10
            currsum.val = add
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None

        return suml.next
            
