class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            # Base case: we reached the end
            if i == len(nums):
                res.append(subset.copy())
                return

            # Choice 1: include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # Choice 2: do not include nums[i]
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res