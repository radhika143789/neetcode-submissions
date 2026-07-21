class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result =[]
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in nums:
                j = nums.index(diff)
                if i != j:
                    result.append(min(i, j))
                    result.append(max(i, j))
                    return result