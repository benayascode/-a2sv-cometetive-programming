class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        out = 0
        for i in range(len(points)-1):
            x = points[i+1][0] - points[i][0]
            out = max(out,x)
        return out 
