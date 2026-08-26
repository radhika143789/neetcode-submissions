class Solution:
    def maxDifference(self, s: str) -> int:
        character = {}
        
        # 1. Count frequencies of all characters first
        for char in s:
            character[char] = character.get(char, 0) + 1
            
        max_odd = float('-inf')
        min_even = float('inf')
        
        # 2. Evaluate the counts AFTER the first loop is completely done
        for count in character.values():
            if count % 2 != 0:       # Check if the frequency is odd
                if count > max_odd:
                    max_odd = count
            elif count % 2 == 0:     # Check if the frequency is even
                if count < min_even:
                    min_even = count
                    
        # 3. Return the calculated difference
        return int(max_odd - min_even)