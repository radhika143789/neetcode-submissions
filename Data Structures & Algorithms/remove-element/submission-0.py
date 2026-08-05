class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k =0
        for num in range(len(nums)):
            if nums[num] != val:
                nums[k] = nums[num]
                k +=1
        return k 
        