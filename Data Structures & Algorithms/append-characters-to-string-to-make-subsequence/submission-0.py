class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        
        # Traverse both strings
        while i < len(s) and j < len(t):
            # If characters match, move the pointer for t
            if s[i] == t[j]:
                j += 1
            # Always move the pointer for s
            i += 1
            
        # The number of characters to append is the remaining length of t
        return len(t) - j