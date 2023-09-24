# 5. Longest Palindromic Substring
# Author: Kevin Zhao
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def manacher(self, S):
        N = len(S)
        A = '@#' + '#'.join(S) + '#$'
        
        dp = [0] * len(A)
        center = right = 0

        for i in range(1, len(A) - 1):
            if i < right: dp[i] = min(right - i, dp[2 * center - i])
                
            while A[i + dp[i] + 1] == A[i - dp[i] - 1]: dp[i] += 1
                
            if i + dp[i] > right: center, right = i, i + dp[i]

        max_len = max(dp)
        max_len_index = dp.index(max_len)
                
        result = A[max_len_index - max_len: max_len_index + max_len + 1]
        
        if result[0] == '#': return result[1::2]

        return result[::2]
    
    def longestPalindrome(self, s: str) -> str:
        return self.manacher(s)
