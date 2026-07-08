class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0

        fp =0
        lp = len(heights)-1 

        while fp<lp:
            area = min(heights[fp], heights[lp]) * (lp-fp)
            if area > ans:
                ans = area
            if heights[fp]< heights[lp]:
                fp+=1
            elif heights[lp] < heights[fp]:
                lp-=1
            else:
                fp+=1
        return ans

