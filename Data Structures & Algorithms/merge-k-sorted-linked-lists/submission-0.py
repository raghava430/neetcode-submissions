# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        # Add the first node of each list to the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        while minHeap:
            val, i, node = heapq.heappop(minHeap)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))

        return dummy.next