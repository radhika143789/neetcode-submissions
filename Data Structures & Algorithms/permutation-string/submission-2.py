class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Corner Case 1: s1 is longer than s2
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        # Initialize the frequency maps for the very first window
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
                
        # Slide the window across s2
        l = 0
        for r in range(len(s1), len(s2)):
            # Corner Case 4: Match found early or mid-string
            if matches == 26:
                return True
                
            # Add new character to the right of the window
            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1
                
            # Remove the character from the left of the window
            index = ord(s2[l]) - ord('a')
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1
            
            l += 1
            
        # Corner Case 4 (cont.): Match found at the very end boundary
        return matches == 26