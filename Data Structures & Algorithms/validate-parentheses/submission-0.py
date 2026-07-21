class Solution:
    def isValid(self, s: str) -> bool:
        # Map each closing bracket to its corresponding opening bracket
        close_to_open = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # If it's a closing bracket
            if char in close_to_open:
                # Pop the top element if stack is not empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping doesn't match the top element, it's invalid
                if close_to_open[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were properly matched
        return not stack