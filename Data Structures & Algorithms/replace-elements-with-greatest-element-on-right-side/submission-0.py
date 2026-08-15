class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        
        # Iterate backwards starting from the last index down to 0
        for i in range(len(arr) - 1, -1, -1):
            # Temporarily store the current value at arr[i]
            current_val = arr[i]
            
            # Replace the current element with the max value found to its right
            arr[i] = right_max
            
            # Update right_max to be the maximum of the current value and the previous right_max
            if current_val > right_max:
                right_max = current_val
                
        return arr
          