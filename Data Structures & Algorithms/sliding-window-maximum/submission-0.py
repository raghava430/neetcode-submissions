from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for r in range(len(nums)):
            # Remove smaller values from the back
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # Remove indexes outside the current window
            if q[0] <= r - k:
                q.popleft()

            # Start adding results once first window is complete
            if r >= k - 1:
                res.append(nums[q[0]])

        return res