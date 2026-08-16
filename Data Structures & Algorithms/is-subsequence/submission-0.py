class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize two pointers at the start of both strings
        i, j = 0, 0
        
        # Loop until one of the pointers reaches the end of its string
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # We found a match, move the pointer for s
            
            j += 1      # Always move the pointer for t to keep searching
        
        # If pointer 'i' reached the end of 's', we found all characters in order
        return i == len(s)