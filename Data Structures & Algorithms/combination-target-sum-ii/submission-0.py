class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        curr = []

        def backtrack(start, total):
            if total == target:
                res.append(curr.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicate choices at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted, no need to continue if too large
                if total + candidates[i] > target:
                    break

                curr.append(candidates[i])

                # i + 1 because each element can be used only once
                backtrack(i + 1, total + candidates[i])

                curr.pop()

        backtrack(0, 0)
        return res