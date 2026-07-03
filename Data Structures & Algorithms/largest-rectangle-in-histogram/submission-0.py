class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                
                maxArea = max(maxArea,(h*width))

            stack.append(i)
        
        n = len(heights)
        while stack:
            h = heights[stack.pop()]

            if stack:
                width = n - stack[-1] - 1
            else:
                width = n
            
            maxArea = max(maxArea,(h*width))

        return maxArea