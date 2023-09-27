# 11. Container With Most Water
# Author: Kevin Zhao
# Runtime: O(n)
# Space : O(1)

# Usually, the trick for this solution is "what about the next height changes my existing solution for the k-1 case?"


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxWater = 0
        while left < right:
            leftHold = height[left]
            rightHold = height[right]

            minHeight = min(leftHold,rightHold)
            currentMaxWater = minHeight * (right - left)
            
            maxWater = max(maxWater, currentMaxWater )

            if leftHold <= rightHold:
                left += 1
            else:
                right -= 1

        return maxWater  # Return the maximum area of water that can be contained.
