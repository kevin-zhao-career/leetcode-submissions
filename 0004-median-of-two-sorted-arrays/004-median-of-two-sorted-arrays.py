# 5. Longest Palindromic Substring
# Author: Kevin Zhao
# Time Complexity: O(n^3)
# Space Complexity: O(1) if we return the indicies, otherwise, O(n) to store the string

# First, we know that we can come up with an O(n^3) brute force solution where for every two indicies, hence o(n^2), we do a
# palindrome check, coming out to O(n^2)O(n) = O(n^3)

def getEndIndex(endIndex : int, difference : int) -> int:
    return (endIndex - difference)

def isPalindrome(string : str) -> bool:
    lastIndex = len(string) - 1
    for index in range(int(len(string) / 2)):
        endIndex = getEndIndex(lastIndex, index)

        if (string[index] != string[endIndex]):
            return False

    return True

class Solution:
    def longestPalindrome(self, string: str) -> str:
        if len(string) <= 1:
            return string
        
        longestPalindromeSubstring = ""
        for beginIndex in range(len(string)):
            for endIndex in range(beginIndex + 1, len(string) + 1):
                substring = string[beginIndex:endIndex]
                longestPalindromeSubstring = (substring if
                    (isPalindrome(substring) and (len(substring) > len(longestPalindromeSubstring))) else longestPalindromeSubstring)

        return longestPalindromeSubstring
