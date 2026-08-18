class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0

        for c in range(len(s) - 1):
            res += abs(ord(s[c]) - ord(s[c+1]))

        return res