class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            # Since the array is sorted, positive starting numbers cannot sum to 0
            if a > 0:
                break
                
            # Skip duplicate values for the first element
            if i > 0 and a == nums[i - 1]:
                continue

            # Two-pointer search for the remaining two numbers
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    # Skip duplicate values for the left pointer
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result