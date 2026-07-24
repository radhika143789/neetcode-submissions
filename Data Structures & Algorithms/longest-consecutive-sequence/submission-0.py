class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set(nums)
        longest_consecutive = 0  # Use consistent naming
        
        for n in sets:
            if n - 1 not in sets:
                current = n
                length = 1
                while current + 1 in sets:
                    current += 1
                    length += 1
                
                longest_consecutive = max(longest_consecutive, length)
                
        return longest_consecutive  # Unindented to return after the loop finishes