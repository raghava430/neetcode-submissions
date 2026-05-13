import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # max heap using negative values
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        # Step 1: Add to maxHeap first
        heapq.heappush(self.small, -num)

        # Step 2: Make sure every number in small <= every number in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: Balance heap sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        if len(self.large) > len(self.small):
            return float(self.large[0])

        return (-self.small[0] + self.large[0]) / 2