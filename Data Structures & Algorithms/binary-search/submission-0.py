class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            
            # Check if the target is found
            if nums[mid] == target:
                return mid
            # If target is greater, ignore the left half
            elif nums[mid] < target:
                left = mid + 1
            # If target is smaller, ignore the right half
            else:
                right = mid - 1
                
        # Target was not found in the array
        return -1
            
        