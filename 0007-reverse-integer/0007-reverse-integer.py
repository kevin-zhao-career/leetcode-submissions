# 7. Reverse Integer
# Author: Kevin Zhao
# Runtime: O(log n)
# Space : O(1)
BASE = 10
INTEGER_MININUM : int = -(2**31)
INTEGER_MAXIMUM : int = (2**31 - 1)

INTEGER_BOUNDARY_RETURN : int = 0

def getIsNegative(integer : int) -> bool:
    return (integer < 0)

def getPositiveInteger(integer : int) -> int:
    return abs(integer)

def integerBoundaryOverflow(isNegative : bool, positiveNumber : int, addend : int) -> bool:
    print("%s %s", positiveNumber, addend)
    return ((-(INTEGER_MININUM + addend) <= positiveNumber) if (isNegative) else
        ((INTEGER_MAXIMUM - addend) <= positiveNumber))

def getLastDigit(number : int) -> int:
    return (number % BASE)

def reverseNumber(isNegative : bool, positiveInteger : int, currentPower : int, reverseIntegerAccumulator : int) -> int:
    if integerBoundaryOverflow(isNegative, reverseIntegerAccumulator, getLastDigit(positiveInteger)):
        return INTEGER_BOUNDARY_RETURN
    if positiveInteger <= 0:
        return -reverseIntegerAccumulator if (isNegative) else reverseIntegerAccumulator
    return reverseNumber(isNegative, int(positiveInteger / BASE), currentPower + 1, (reverseIntegerAccumulator * BASE) + getLastDigit(positiveInteger))

class Solution:
    def reverse(self, integer: int) -> int:
        if (integer == 0):
            return 0
        return reverseNumber(getIsNegative(integer), getPositiveInteger(integer), 0, 0)
