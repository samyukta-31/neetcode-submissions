# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode()
        curr = newNode

        if not list1 and not list2:
            return None
        elif not list1 and list2:
            return list2
        elif list1 and not list2:
            return list1
        else:
            curr1 = list1
            curr2 = list2
            while curr1 or curr2:
                if not curr1:
                    curr.next = curr2
                    return newNode.next
                elif not curr2:
                    curr.next = curr1
                    return newNode.next
                if curr1.val < curr2.val:
                    curr.next = curr1
                    curr1 = curr1.next
                elif curr1.val >= curr2.val:
                    curr.next = curr2
                    curr2 = curr2.next
                curr = curr.next
        
        return newNode.next
