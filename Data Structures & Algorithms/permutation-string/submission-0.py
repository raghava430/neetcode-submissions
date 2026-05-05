class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        for ch in s1:
            s1_count[ord(ch) - ord('a')] += 1

        l = 0

        for r in range(len(s2)):
            window_count[ord(s2[r]) - ord('a')] += 1

            if r - l + 1 > len(s1):
                window_count[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if window_count == s1_count:
                return True

        return False