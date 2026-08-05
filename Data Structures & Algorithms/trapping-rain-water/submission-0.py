class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l ,r =0 , len(height)-1
        left_max ,right_max =height[l] ,height[r]
        total=0
        while l < r:
            # We always process the side with the smaller max height
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                # Water trapped is the left_max minus current height
                total += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                # Water trapped is the right_max minus current height
                total += right_max - height[r]

        return total