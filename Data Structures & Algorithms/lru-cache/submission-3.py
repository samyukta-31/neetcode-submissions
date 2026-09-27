class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node:ListNode):
        node.prev.next = node.next # prev.next
        node.next.prev = node.prev # next.prev

    def insert_at_end(self, node:ListNode):
        last = self.tail.prev
        last.next = node
        node.next = self.tail
        node.prev = last
        self.tail.prev = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.insert_at_end(node)
            return node.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            node.val = value
            self.insert_at_end(node)
        else:
            if len(self.cache) == self.capacity:
                lru = self.head.next
                self.remove_node(lru) # removing lru
                del self.cache[lru.key]
            node = ListNode(key, value)
            self.cache[key] = node
            self.insert_at_end(node)
        
