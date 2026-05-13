class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        used = [False] * len(nums)

        def backtrack():
            # Base case: current permutation is complete
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                # Skip numbers already used in current permutation
                if used[i]:
                    continue

                # Choose nums[i]
                used[i] = True
                curr.append(nums[i])

                # Explore
                backtrack()

                # Undo choice
                curr.pop()
                used[i] = False

        backtrack()
        return res