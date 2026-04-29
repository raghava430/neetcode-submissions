class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, i: int) -> int:
        if i < 0 or i >= self.size:
            return -1

        curr = self.head
        for _ in range(i):
            curr = curr.next

        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

        if self.size == 0:
            self.tail = new_node

        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        if self.size == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def remove(self, i: int) -> bool:
        if i < 0 or i >= self.size:
            return False

        # Remove head
        if i == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
            self.size -= 1
            return True

        # Remove non-head
        prev = self.head
        for _ in range(i - 1):
            prev = prev.next

        node_to_remove = prev.next
        prev.next = node_to_remove.next

        # If removing tail
        if node_to_remove == self.tail:
            self.tail = prev

        self.size -= 1
        return True

    def getValues(self) -> list:
        result = []
        curr = self.head

        while curr:
            result.append(curr.val)
            curr = curr.next

        return result