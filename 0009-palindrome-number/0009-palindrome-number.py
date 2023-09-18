# 9. Palindrome Number
# Time Complexity: O(log n)
# Space Complexity: O(1)

def getLastDigit(integer : int) -> bool:
    return (integer % 10)

def isZero(integer : int) -> bool:
    return (integer == 0)

def endsWithZero(integer : int) -> bool:
    return (getLastDigit(integer) == 0)

def isInvalidArgument(integer : int) -> bool:
    return (integer < 0) or (integer != 0 and endsWithZero(integer))

class Solution:
    def isPalindrome(self, integer: int) -> bool:
        if isZero(integer):
            return True

        if isInvalidArgument(integer):
            return False

        reversed_number = 0
        original = integer

        while integer > reversed_number:
            reversed_number = (reversed_number * 10) + getLastDigit(integer)
            integer //= 10

        return (integer == reversed_number) or (integer == reversed_number // 10)
