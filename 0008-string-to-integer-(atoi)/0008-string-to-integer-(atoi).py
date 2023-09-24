# 8. String to Integer (atoi)
# Author: Kevin Zhao
# Time Complexity: O(n)
# Space Complexity: O(1) because it is the space of the integer

INT_MINIMUM = -2**31
INT_MAXIMUM = 2**31-1

POSITIVE_SIGN = '+'
NEGATIVE_SIGN = '-'

ZERO_ORDINAL = ord('0')
BASE = 10

NOT_A_DIGIT_EXCEPTION = "%s is not a digit"

def getDigit(character : str) -> int:
    if not character.isdigit():
        raise ValueError(NOT_A_DIGIT_EXCEPTION.format(character))
    return (ord(character) - ZERO_ORDINAL)

def getNumber(isNegative : bool, positiveNumber : int) -> int:
    return (-positiveNumber) if isNegative else (positiveNumber)

def getNonWhitespaceCharacterBeginIndex(string : str) -> int:
    return next((index for index, character in enumerate(string) if not character.isspace()), len(string))

def getIsNegative(character : str) -> bool:
    return (character == NEGATIVE_SIGN)

def isSignCharacter(character : str) -> bool:
    return (character == NEGATIVE_SIGN) or (character == POSITIVE_SIGN)

def getBeginIndex(string : str, beginIndex : int) -> int:
    if beginIndex >= len(string):
        return beginIndex
    character = string[beginIndex]

    return (beginIndex + 1) if isSignCharacter(character) else (beginIndex)

def hitIntegerBoundary(isNegative : bool, currentPositiveInteger : int, currentDigit : int) -> bool:
    comparisonNumber = (-(INT_MINIMUM + currentDigit)) if isNegative else (INT_MAXIMUM - currentDigit)
    return (comparisonNumber / BASE) <= currentPositiveInteger

def getRespectiveSignedBoundary(isNegative : bool) -> int:
    return (INT_MINIMUM) if isNegative else (INT_MAXIMUM)

def updateCurrentPositiveInteger(currentPositiveInteger : int, nextDigit : int) -> int:
    return (currentPositiveInteger * BASE) + nextDigit

class Solution:
    def myAtoi(self, string: str) -> int:      
        nonWhitespaceCharacterBeginIndex = getNonWhitespaceCharacterBeginIndex(string)
        if nonWhitespaceCharacterBeginIndex >= len(string):
            return 0
        isNegative = getIsNegative(string[nonWhitespaceCharacterBeginIndex])

        currentPositiveInteger = 0
        beginIndex = getBeginIndex(string, nonWhitespaceCharacterBeginIndex)

        for index in range(beginIndex, len(string)):
            try:
                character = string[index]
                currentDigit = getDigit(character)

                if hitIntegerBoundary(isNegative, currentPositiveInteger, currentDigit):
                    return getRespectiveSignedBoundary(isNegative)

                currentPositiveInteger = updateCurrentPositiveInteger(currentPositiveInteger, currentDigit)
            except Exception as error:
                break

        return getNumber(isNegative, currentPositiveInteger)
        
