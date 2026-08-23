class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l = 0
        for r in range(len(s)):
            if l == len(t) :
                return 0
            if t[l] == s[r] :
                l+=1
        return len(t) - l
                    
        