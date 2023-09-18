# 9. Palindrome Number
# Time Complexity: O(log n)
# Space Complexity: O(1)

def getLastDigit(integer : int):
    return (integer % 10)

def endsWithZero(integer : int):
    return (getLastDigit(integer) == 0)

def isInvalidArgument(integer : int):
    return (integer < 0) or (integer != 0 and endsWithZero(integer))

class Solution:
    def isPalindrome(self, integer: int) -> bool:
        if isInvalidArgument(integer):
            return False

        reversed_num = 0
        original = integer

        while integer > reversed_num:
            reversed_num = reversed_num * 10 + getLastDigit(integer)
            integer //= 10

        return integer == reversed_num or integer == reversed_num // 10
