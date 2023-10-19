# 42. Trapping Rain Water
# Author: Kevin Zhao
# Time Complexity: O(n)
# Space Complexity: O(1)
import sys

class Solution:
    def trap(self, heights: List[int]) -> int:
        leftIndex = 0
        rightIndex = len(heights) - 1
        
        leftMaximum = -sys.maxsize -1 
        rightMaximum = -sys.maxsize -1 
        
        ans=0
        while(leftIndex < rightIndex):
            leftMaximum = max(leftMaximum, heights[leftIndex])
            rightMaximum = max(rightMaximum, heights[rightIndex])
            ans += (leftMaximum - heights[leftIndex]) if (leftMaximum < rightMaximum) else rightMaximum-heights[rightIndex];
            
            if (leftMaximum < rightMaximum):
                leftIndex += 1
            else:
                rightIndex -= 1
        return ans;
