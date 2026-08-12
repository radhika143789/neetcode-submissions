class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        total_xor = 0
        for num in nums:
            total_xor |= num
       
        return total_xor << (len(nums) - 1)