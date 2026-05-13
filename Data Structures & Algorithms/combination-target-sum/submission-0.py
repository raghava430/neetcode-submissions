class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def backtrack(start, total):
            # Base case 1: valid combination
            if total == target:
                res.append(curr.copy())
                return

            # Base case 2: sum became too large
            if total > target:
                return

            for i in range(start, len(nums)):
                curr.append(nums[i])

                # i, not i + 1, because we can reuse nums[i]
                backtrack(i, total + nums[i])

                curr.pop()

        backtrack(0, 0)
        return res