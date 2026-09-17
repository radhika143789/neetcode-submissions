class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
             stack = []
             max_area = 0

             heights.append(0)

             for i, height in enumerate(heights):

                while stack and heights[stack[-1]] > height:
                    mid = stack.pop()

                    h = heights[mid]

                    width = i if not stack else i - stack[-1] - 1

                    max_area = max(max_area, h * width)

                stack.append(i)

             return max_area