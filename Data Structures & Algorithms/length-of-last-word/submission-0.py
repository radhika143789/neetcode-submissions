class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 1. You must assign the stripped string back to 's'
        s = s.strip() 
        count = 0
        
        for i in s:
            # 2. Check if the character 'i' is actually a space
            if i == ' ': 
                count = 0  # Reset count for the next word
            else:
                count += 1 # Add 1 for every letter
                
        # 3. By the end of the loop, count holds the length of the last word
        return count