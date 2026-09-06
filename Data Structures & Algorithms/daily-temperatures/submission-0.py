class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        # The stack will store the indices of the temperatures
        stack = [] 

        for i, t in enumerate(temperatures):
            # While stack is not empty and current temp is greater 
            # than the temp at the index stored at the top of the stack
            while stack and t > temperatures[stack[-1]]:
                prev_index = stack.pop()
                # The number of days is the difference between current index and popped index
                res[prev_index] = i - prev_index
            
            # Add the current day's index to the stack to wait for a warmer day
            stack.append(i)

        return res