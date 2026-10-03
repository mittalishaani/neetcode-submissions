class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        watercap=0
        leftmax = [0] * n
        rightmax = [0] * n
        leftmax[0] = height[0]
        rightmax[n - 1] = height[n - 1]
        for i in range(n):
            leftmax[i] = max(leftmax[i - 1], height[i])
        for i in range(n-2, -1, -1):#have to go reverse order, and to skip the last column
            rightmax[i] = max(rightmax[i + 1], height[i])
        for i in range(n):
            watercap+= min(leftmax[i], rightmax[i]) - height[i]
        return watercap