from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map character count to list of anagrams
        ans = defaultdict(list)
        
        for s in strs:
            # Create a count array of size 26 for 'a' to 'z'
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # Tuples are immutable and hashable, making them valid dictionary keys
            ans[tuple(count)].append(s)
            
        return list(ans.values())