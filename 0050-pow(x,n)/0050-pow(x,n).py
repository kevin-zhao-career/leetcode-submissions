# 50. Pow(x, n)
# Author: Kevin Zhao
# Time Complexity: O(log n)
# Space Complexity: O(1)

ZERO_EXPONENTIAL = 1

def getIsNegative(number : int) -> bool:
    return (number < 0)

def getPositivePower(power : int) -> int:
    return abs(power)

def isOdd(number : int) -> bool:
    return (number % 2 != 0)

def getExponentialNumber(isNegativePower : bool, base: float, positivePower: int, numberAccumulate : int = 1) -> float :
    if getIsNegative(positivePower):
        return getExponentialNumber(not isNegativePower, base, positvePower, numberAccumulate)
    if positivePower == 0:
        return (1.0/numberAccumulate) if isNegativePower else numberAccumulate
    if (base == 0):
        return (1/0) if (isNegativePower) else (0)
    if isOdd(positivePower):
        return getExponentialNumber(isNegativePower, base * base, positivePower >> 1, numberAccumulate * base)
    return getExponentialNumber(isNegativePower, base * base, positivePower >> 1, numberAccumulate)   

class Solution:
    def myPow(self, base: float, power: int) -> float:
        positivePower = getPositivePower(power)
        isNegativePower = getIsNegative(power)

        return getExponentialNumber(isNegativePower, base, positivePower, 1)
