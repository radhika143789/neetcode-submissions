class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n
        
        # Step 1: Compute prefix products (everything to the left of index i)
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Multiply by suffix products (everything to the right of index i)
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
            
        return result