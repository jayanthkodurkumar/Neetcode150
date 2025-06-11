class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # remove it
            self.remove(node)
            # insert it at end
            self.insert(node)
            # return node val
            return node.value

        # return -1 if key is not there
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove it
            self.remove(self.cache[key])

        if len(self.cache) == self.capacity:
            # remove lru
            self.remove(self.tail.prev)

        # insert node at the start as head's next and update
        new_node = Node(key, value)
        self.insert(new_node)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.cache.pop(node.key)

    def insert(self, node):
        self.cache[node.key] = node

        node.next = self.head.next
        self.head.next.prev = node

        self.head.next = node
        node.prev = self.head


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
