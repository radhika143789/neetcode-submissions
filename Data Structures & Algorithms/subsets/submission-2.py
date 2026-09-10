class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def fun(idx,arr):
            if idx>=n:
                ans.append(arr.copy())
                return
            
            arr.append(nums[idx])
            fun(idx+1, arr)

            arr.pop()
            fun(idx+1, arr)
        
        fun(0,[])

        return ans
