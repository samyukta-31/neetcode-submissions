# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorted_ll = ListNode(0)
        for l in lists:
            curr_l = l
            prev_sll = sorted_ll

            while curr_l:
                while prev_sll.next and prev_sll.next.val < curr_l.val:
                    prev_sll = prev_sll.next
                else:
                    next_sorted = prev_sll.next # save what has to come after insert
                    next_curr = curr_l.next
                    curr_l.next = next_sorted # joining remaining sorted list to what is being inserted
                    prev_sll.next = curr_l # insert after what has passed
                curr_l = next_curr
            prev_sll = sorted_ll
        return sorted_ll.next