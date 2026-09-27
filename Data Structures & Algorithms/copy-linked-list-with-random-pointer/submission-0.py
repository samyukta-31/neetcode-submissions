"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        prev = Node(0)
        currp = prev
        currh = head
        copies = {}

        while currh:
            currp.next = Node(currh.val)
            copies[currh] = currp.next
            currh = currh.next
            currp = currp.next

        currp = prev.next
        currh = head
        while currh:
            currp.random = copies[currh.random] if currh.random in copies else None
            currp.next = copies[currh.next] if currh.next in copies else None
            currp = currp.next
            currh = currh.next

        return prev.next

