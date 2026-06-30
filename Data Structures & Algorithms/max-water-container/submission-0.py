class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_a = float('-inf')
        while(i<j):
            area = (j-i) * (min(heights[i],heights[j]))
            max_a = max(max_a,area)
            if(heights[i] < heights[j]):
                i +=1
            else:
                j -= 1
        return max_a