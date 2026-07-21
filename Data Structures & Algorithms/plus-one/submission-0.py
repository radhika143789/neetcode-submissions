class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 'for' is indented here
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If the digit is 9, it becomes 0 and we carry the 1 to the next loop iteration
            digits[i] = 0
            
        # 'return' must align perfectly with 'for'
        return [1] + digits