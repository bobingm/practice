class DoubleListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.hashmap = {}
        self.head = None
        self.tail = None

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key in self.hashmap:
            node = self.hashmap[key]
            self.move_to_tail(node)
            return node.val
        # print "bbb"
        return -1

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        occupied = len(self.hashmap)
        # remove head
        if occupied == self.capacity:
            node = self.remove_head()
            del self.hashmap[node.key]

        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.move_to_tail(node)
        else:
            node = DoubleListNode(key, value)
            self.hashmap[key] = node
            self.insert(node)
        
    
    def remove_head(self):
        node = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        return node
    
    def insert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next

    
    def move_to_tail(self, node):
        if self.head == node:
            self.remove_head()
            self.insert(node)
        elif self.tail == node:
            pass
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.insert(node)
        

if __name__ == "__main__":
    pass