class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        count = 0

        while count < len(nums) - 1:
            if nums[count] == nums[count + 1]:
                nums.pop(count)
            else:
                count += 1

        return len(nums)


