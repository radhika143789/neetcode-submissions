class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(word) -> bool:
            left =0
            right = len(word)-1
            print(word)
            while left<right:
                if word[left]!= word[right]:
                    return False
                left+=1
                right-=1
            return True

        left =0
        right = len(s)-1
        while left<right:
            if s[left]!= s[right]:
                return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
            left+=1
            right-=1
        return True