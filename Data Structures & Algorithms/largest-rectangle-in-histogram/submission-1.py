class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        left = [-1]*len(heights)
        right = [len(heights)]*len(heights)

        stack = []
        for i in range(len(heights)):
            while stack and (heights[stack[-1]] >= heights[i]):
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(len(heights)-1, -1, -1):
            while stack and (heights[stack[-1]] >= heights[i]):
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        for i in range(len(heights)):
            max_area = max(max_area, (right[i]-left[i]-1)*heights[i])
        return max_area