class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str1 = list(word1)
        str2 =list (word2)
        c1 = 0
        c2= 0
        result = []
        while c1 < len(word1) or c2 < len(word2):
            # Check if c1 is still within bounds before appending
            if c1 < len(word1):
                result.append(word1[c1])
                c1 += 1
                
            # Check if c2 is still within bounds before appending
            if c2 < len(word2):
                result.append(word2[c2])
                c2 += 1
                
        # Convert the resulting list back into a single string
        return "".join(result)