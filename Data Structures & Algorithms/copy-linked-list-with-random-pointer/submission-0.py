class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        # First pass: create copy nodes
        curr = head
        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: assign next and random pointers
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]