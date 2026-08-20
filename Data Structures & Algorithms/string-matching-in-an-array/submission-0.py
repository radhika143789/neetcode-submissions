class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # empty array 
        result = []
        
        # looping every word to pick target
        for i in range(len(words)):
            # loopin through every word again to pick comparer
            for j in range(len(words)):
                
                # Make sure they aren't the exact same word
                if i != j:
                    
                    # Check if word 'i' is inside word 'j'
                    if words[i] in words[j]:
                        result.append(words[i])
                        break # Stop checking this word to avoid duplicates
        
        # Return the final list outside of all loops
        return result