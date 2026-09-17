class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_h = 0
        stack = [(0, -1)]

        for idx, h in enumerate(heights):
            if not stack or stack[-1][0] < h:
                stack.append((h, idx))
            elif stack[-1][0] > h:
                p_idx = idx

                while stack and stack[-1][0] > h:
                    p_h, p_idx = stack.pop()
                    max_h = max(max_h, p_h * (idx - p_idx))

                stack.append((h, p_idx))

        while stack:
            h, idx = stack.pop()
            max_h = max(max_h, h * (len(heights) - idx))

        return max_h
