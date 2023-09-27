# 50. Pow(x, n)
# Author: Kevin Zhao
# Time Complexity: O(log n)
# Space Complexity: O(1)

ZERO_EXPONENTIAL = 1

def getIsNegative(number : int) -> bool:
    return (number < 0)

def getPositivePower(power : int) -> int:
    return abs(power)

def getExponentialNumber(isNegativePower : bool, number : float) -> float :
    return (1.0 / number) if (isNegativePower) else number

def isOdd(number : int) -> bool:
    return (number % 2 != 0)

class Solution:
    def myPow(self, base: float, power: int) -> float:
        if (power == 0):
            return ZERO_EXPONENTIAL
        if (base == 0):
            return 0 if (power > 0) else (1/0)

        remainingPositivePower = getPositivePower(power)
        isNegative = getIsNegative(power)
        
        numberAccumulate = 1
        currentBase = base
        while remainingPositivePower > 0:
            if (isOdd(remainingPositivePower)):
                numberAccumulate *= currentBase
            
            currentBase *= currentBase
            remainingPositivePower >>= 1


        return getExponentialNumber(isNegative, numberAccumulate)
