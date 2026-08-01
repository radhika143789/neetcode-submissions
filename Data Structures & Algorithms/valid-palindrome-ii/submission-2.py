class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # A mismatch is found. 
                # Try skipping the left character OR the right character.
                skip_l = s[l + 1 : r + 1]
                skip_r = s[l : r]
                
                # Check if either resulting substring is a palindrome
                return (skip_l == skip_l[::-1]) or (skip_r == skip_r[::-1])
                
        return True