class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charCounter = {}
        for char in s:
            if char not in charCounter:
                charCounter[char] =1
            else:
                charCounter[char] +=1
        for char in t:
            if char not in charCounter:
                return False
            else:
                charCounter[char] -=1
            if charCounter[char] <0:
                return False
        return True