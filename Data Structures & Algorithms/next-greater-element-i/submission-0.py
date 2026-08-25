class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_map = {}
        stack = []
        
        # 1. Find the next greater element for everything in nums2
        for num in nums2:
            # While stack is not empty and current number is greater than top of stack
            while stack and num > stack[-1]:
                # We found the next greater element for the number at the top of the stack
                smaller_num = stack.pop()
                next_greater_map[smaller_num] = num
            
            # Add the current number to the stack to find its next greater element later
            stack.append(num)
            
        # 2. Build the result array for nums1
        result = []
        for num in nums1:
            # Look up the next greater element in our map, default to -1 if not found
            result.append(next_greater_map.get(num, -1))
            
        return result
        