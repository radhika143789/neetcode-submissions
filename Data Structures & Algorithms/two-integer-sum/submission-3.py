class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       my_dict = {} # {32 : 0, 24 : 1, ... , 29 : len(nums) - 1}
       for i in range(0, len(nums)):
            if (target - nums[i]) in my_dict:
                return [my_dict[target - nums[i]], i]
            my_dict[nums[i]] = i