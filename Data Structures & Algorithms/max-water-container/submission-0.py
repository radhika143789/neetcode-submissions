class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        l = len(heights)-1
        area =0
        while i <l:
            current =(l-i)*min(heights[i],heights[l])
            area = max(current,area)
            if heights[i] < heights[l]:
                i += 1
            else:
                l -= 1
        return area