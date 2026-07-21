import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The minimum eating speed is 1
        # The maximum eating speed is the size of the largest pile
        left = 1
        right = max(piles)
        
        # Keep track of the minimum valid speed found so far
        res = right 
        
        while left <= right:
            k = (left + right) // 2
            
            # Calculate how many hours it takes at speed 'k'
            total_hours = 0
            for pile in piles:
                # math.ceil ensures any remainder takes a full hour
                total_hours += math.ceil(pile / k) 
                
            # If Koko can finish within h hours, this speed works.
            # But let's check if she can go even slower (search left).
            if total_hours <= h:
                res = k
                right = k - 1
            # If it takes too long, she needs to eat faster (search right).
            else:
                left = k + 1
                
        return res