class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
      # If no flowers need to be planted, it's always possible
        if n == 0:
            return True
            
        for i in range(len(flowerbed)):
            # Check if the current plot is empty
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty or if we are at the edges
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # If both adjacent plots are empty, we can plant a flower
                if empty_left and empty_right:
                    flowerbed[i] = 1  # Plant the flower
                    n -= 1            # Decrement the remaining flowers to plant
                    
                    # If we've planted all required flowers, we can return early
                    if n == 0:
                        return True
                        
        # If we finish the loop and haven't reached n == 0, return False
        return n <= 0