# 1739. Building Boxes
# Author: Kevin Zhao
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def minimumBoxes(self, n: int) -> int:
        p = -1
        q = 3*n
        r = 2/3
        m = floor((q + (q**2 + (r - p**2)**3)**(1/2))**(1/3) + (q - (q**2 + (r - p**2)**3)**(1/2))**(1/3) + p + 0.0001)
    
        diff = n - (m)*(m+1)*(m+2)//6
        return ceil(((1 + 8*diff)**0.5 - 1)/2) + (m*(m+1))//2
