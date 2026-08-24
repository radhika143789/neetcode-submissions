class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

        