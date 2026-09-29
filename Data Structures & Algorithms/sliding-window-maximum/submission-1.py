class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = k
        loc_max = max(nums[0:k])
        out = []
        out.append(loc_max)

        while l < len(nums):
            if nums[l - k] == loc_max:
                if k > 1:
                    loc_max = max(nums[l-k+1:l])
                else:
                    loc_max = -10000
            
            if nums[l] > loc_max:
                loc_max = nums[l]
            
            out.append(loc_max)
            
            l += 1

        return out