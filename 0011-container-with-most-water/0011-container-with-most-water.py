class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        n = len(heights)
        i = 0
        j = n-1
        while i <= n and j >= 0:
            best = max((abs(j-i)*min(heights[i], heights[j])), best)
            if heights[i] >= heights[j]:
                j -= 1
            elif heights[j] > heights[i]:
                i += 1
        return best

