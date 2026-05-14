from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        path = []

        def backtrack(i):
            # If we formed one full combination
            if i == len(digits):
                res.append("".join(path))
                return

            digit = digits[i]
            letters = digit_to_letters[digit]

            for ch in letters:
                path.append(ch)
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res