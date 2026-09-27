# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(None)
        prev.next = head
        fp = prev
        sp = prev
        count = 0
        while count < n+1:
            fp = fp.next
            count += 1
        while fp:
            fp = fp.next
            sp = sp.next
        sp.next = sp.next.next if sp and sp.next else None

        return prev.next
        
        # # plan: reverse the linked list, remove the nth element and reverse it again

        # prev = None
        # curr = head
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        
        # # prev is the reversed linked list
        # count = 1
        # curr = prev
        # previous = None
        # while curr and count<=n:
        #     print(curr.val, count)
        #     if count == n:
        #         previous.next = curr.next
        #         previous = curr
        #     else:
        #         previous = curr
        #         curr = curr.next
        #     count += 1
        
        # # reverse again
        # previous = None
        # curr = prev
        # while curr:
        #     nxt = curr.next
        #     curr.next = previous
        #     previous = curr
        #     curr = nxt
        # return previous
