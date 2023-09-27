# 11. Container With Most Water
# Author: Kevin Zhao
# Runtime: O(n)
# Space : O(1)

# Usually, the trick for this solution is "what about the next height changes my existing solution for the k-1 case?"


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1  # Initialize two pointers, left and right, pointing to the start and end of the height list respectively.
        out = 0  # Initialize the maximum area to 0.

        while left < right:  # Continue the loop until the pointers meet or cross each other.
            area = min(height[left], height[right]) * (right - left)  # Calculate the area of the container formed by the current left and right boundaries.
            out = max(out, area)  # Update the maximum area if the current area is greater.

            if height[left] < height[right]:  # If the height at the left pointer is smaller than the height at the right pointer:
                left += 1  # Move the left pointer to the right.
            else:  # If the height at the left pointer is greater than or equal to the height at the right pointer:
                right -= 1  # Move the right pointer to the left.

        return out  # Return the maximum area of water that can be contained.
