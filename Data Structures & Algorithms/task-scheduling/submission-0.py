import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        # Max heap using negative counts
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)

        # queue stores: [remaining_count, available_time]
        q = deque()

        time = 0

        while heap or q:
            time += 1

            if heap:
                count = heapq.heappop(heap)
                count += 1  # because count is negative

                if count != 0:
                    q.append([count, time + n])

            if q and q[0][1] == time:
                available_count, available_time = q.popleft()
                heapq.heappush(heap, available_count)

        return time