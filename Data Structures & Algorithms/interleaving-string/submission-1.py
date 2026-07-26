class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        dp = {}
        
        # i is the pointer for s1, j is the pointer for s2
        def dfs(i, j):
            # Base case: If both pointers reach the end, we successfully matched everything
            if i == len(s1) and j == len(s2):
                return True
                
            # If we've already solved for this state, return the cached result
            if (i, j) in dp:
                return dp[(i, j)]
            
            # The current index in s3 is just the sum of i and j
            k = i + j 
            
            # Branch 1: Try using a character from s1
            if i < len(s1) and s1[i] == s3[k] and dfs(i + 1, j):
                return True
                
            # Branch 2: Try using a character from s2
            if j < len(s2) and s2[j] == s3[k] and dfs(i, j + 1):
                return True
                
            # If neither branch works, cache the failure and return False
            dp[(i, j)] = False
            return False
            
        return dfs(0, 0)