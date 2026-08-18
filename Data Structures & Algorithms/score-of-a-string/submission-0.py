class Solution:
    def scoreOfString(self, s: str) -> int:
       ascii = [ord(char) for char in s]
       score = 0
       for i in range(len(ascii) - 1):
        score += abs(ascii[i] - ascii[i+1])
       return score