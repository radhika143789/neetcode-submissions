class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_val = 0
        for num in nums:
            if num != val:
                nums[last_val] = num
                last_val += 1
        
        return last_val
                

