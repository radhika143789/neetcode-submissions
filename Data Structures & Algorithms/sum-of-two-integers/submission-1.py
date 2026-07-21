class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        
        def helper(a, b):
            # Base case: if there is no carry, return 'a'
            if b == 0:
                # Handle two's complement for Python's arbitrary integers
                return a if a <= MAX_INT else ~(a ^ MASK)
            
            # Sum without carry
            sum_without_carry = (a ^ b) & MASK
            # Carry shifted left
            carry = ((a & b) << 1) & MASK
            
            return helper(sum_without_carry, carry)
            
        return helper(a & MASK, b & MASK)