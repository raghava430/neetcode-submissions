from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def isPalindrome(sub):
            return sub == sub[::-1]

        def backtrack(start):
            # If we used the whole string, save this partition
            if start == len(s):
                res.append(path.copy())
                return

            # Try every possible ending position
            for end in range(start, len(s)):
                substring = s[start:end + 1]

                if isPalindrome(substring):
                    path.append(substring)
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return res