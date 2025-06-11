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
            self.move_to_tail(node)

            # return node val
            return node.value

        # return -1 if key is not there
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # move node to tail and update value
            node = self.cache[key]
            self.move_to_tail(node)
            node.value = value
        else:
            if len(self.cache) == self.capacity:
                # move lru at head to tail and then change its <key, value>
                node = self.head.next
                self.cache.pop(node.key)

                self.move_to_tail(node)

                node.key = key
                node.value = value
                self.cache[key] = node
            else:
                node = Node(key, value)
                self.insert(node)
                self.cache[key] = node

    def move_to_tail(self, node):
        # delink the node
        self.remove(node)
        self.insert(node)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        # connect the node and tail's prev
        node.prev = self.tail.prev
        node.prev.next = node
        # connect node and tail
        self.tail.prev = node
        node.next = self.tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
