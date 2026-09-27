# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
            
        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy
        curr = head
        temp = curr
        
        while temp:
            count = 0
            prev = None
            group_head = curr
            while temp and count < k:
                count += 1
                temp = temp.next
                continue
            if count < k:
                break
            else:
                # reversing 
                while curr and curr != temp:
                    next_curr = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next_curr
                prev_group_tail.next = prev # mimicking curr.next = prev
                prev_group_tail = group_head # mimicking prev = curr
                group_head.next = curr
            temp = curr
        return dummy.next

