# 4. Median of Two Sorted Arrays
# Author: Kevin Zhao
# Runtime: O(log (m + n))
# Space: O(1)

# The trick is if we see a question such as a sorted array, the hunch is to use something like binary search to bring the runtime
# to log(n). In this case, it should be a modified binary search.

NEGATIVE_INFINITY_FLOAT : float = float('-inf')
POSITIVE_INFINITY_FLOAT : float = float('inf')

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        n = n1 + n2
        left = (n1 + n2 + 1) // 2
        low, high = 0, n1
        
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
            
            l1 = NEGATIVE_INFINITY_FLOAT if mid1 == 0 else nums1[mid1 - 1]
            l2 = NEGATIVE_INFINITY_FLOAT if mid2 == 0 else nums2[mid2 - 1]
            r1 = POSITIVE_INFINITY_FLOAT if mid1 == n1 else nums1[mid1]
            r2 = POSITIVE_INFINITY_FLOAT if mid2 == n2 else nums2[mid2]
            
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        
        return 0.0
