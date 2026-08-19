class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum =0
        count =0
        for binary in nums:
            if binary==1:
                count +=1
                maximum = max(maximum,count)
            
            else:
                count =0
        return maximum