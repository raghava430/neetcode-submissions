import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = x * x + y * y

            # Use negative distance to simulate max heap
            heapq.heappush(heap, (-dist, x, y))

            # If heap has more than k points, remove farthest point
            if len(heap) > k:
                heapq.heappop(heap)

        return [[x, y] for dist, x, y in heap]