class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen =[]
        for i in nums:
            if i in seen:
                return i
            else:
                seen.append(i)
        return -1
