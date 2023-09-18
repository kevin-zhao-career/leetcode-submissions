# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
   def maximumSum(self, A: List[int]) -> int:
        return max(sum(A[k * v * v - 1] for v in range(1, isqrt(len(A) // k) + 1)) for k in range(1, len(A) + 1))
