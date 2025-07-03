class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        temp = image[sr][sc]
        image[sr][sc] = color
        if sr-1 != -1 and temp == image[sr-1][sc] and temp != color:
            Solution().floodFill(image, sr-1, sc, color)
        try:
            if temp == image[sr+1][sc] and temp != color:
                Solution().floodFill(image, sr+1, sc, color)
        except:
            pass
        if sc-1 != -1 and temp == image[sr][sc-1] and temp != color:
            Solution().floodFill(image, sr, sc-1, color)
        try:
            if temp == image[sr][sc+1] and temp != color:
                Solution().floodFill(image, sr, sc+1, color)
        except:
            pass
        return image


