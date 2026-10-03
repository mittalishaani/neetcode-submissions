class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxcap = 0
        while l < r:
            cap = (min(heights[l], heights[r])) * (r - l)
            maxcap = max(cap, maxcap)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return maxcap
