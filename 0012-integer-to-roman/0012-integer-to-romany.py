# 12. Integer to Roman
# Author: Kevin Zhao
# Time Complexity: O(1)
# Space Complexity: O(1)

from collections import OrderedDict

BASE = 10
HALFWAY_BASE = (BASE / 2)

ROMAN_NUMERAL_LIST : List[str] = ["I", "V", "X", "L", "C", "D", "M"]

def isEven(number : int) -> bool:
    return ((number % 2) == 0)

def isMultipleOfFive(number : int) -> bool:
    return ((number % 5) == 0)

def oneAwayMultipleOfFive(number : int) -> bool:
    return isMultipleOfFive(number + 1)

def getBaseFiveString(digit : int) -> str:
    return ROMAN_NUMERAL_LIST[digit]

def generateNumberLists(singleDigitString : str, fiveDigitString : str, tenDigitString) -> List[str]:
    numberList = []
    for number in range(0, BASE):
        if oneAwayMultipleOfFive(number):
            baseFiveString = tenDigitString if (number >= 9) else fiveDigitString
            numberList.append(singleDigitString + baseFiveString)
            continue
        else:
            singleDigitNumber = (number - 5) if (number >= 5) else number
            baseFiveString = fiveDigitString if (number >= 5) else ""
            numberList.append(baseFiveString + (singleDigitString * singleDigitNumber))

    return numberList

def getBaseTenOrderedDict(maximumBasePower : int) -> OrderedDict[int, List[str]]:
    baseTenOrderedDict = OrderedDict([])
    romanNumeralListLength = len(ROMAN_NUMERAL_LIST)
    for basePower in range(0, maximumBasePower):
        initalBase = min(basePower * 2, (romanNumeralListLength - 1))
        initalBase2 = min(initalBase + 1, (romanNumeralListLength - 1))
        initalBase3 = min(initalBase + 2, (romanNumeralListLength - 1))
        baseTenOrderedDict[BASE**basePower] = generateNumberLists(ROMAN_NUMERAL_LIST[initalBase],
                    ROMAN_NUMERAL_LIST[initalBase2],
                    ROMAN_NUMERAL_LIST[initalBase3])
    return baseTenOrderedDict

NUMBER_POWER_TO_LETTER_LISTS = getBaseTenOrderedDict(4)

def getDigit(number : int, currentPower : int) -> int:
    return int((number % (currentPower * BASE)) / currentPower)

def getRomanNumeralString(number : int, currentBasePower :int, romanNumeralStringList : List[str]) -> str:
    currentPower = BASE**currentBasePower
    letterList = NUMBER_POWER_TO_LETTER_LISTS[currentPower]
    digit = getDigit(number, currentPower)
    letters = letterList[digit]
    romanNumeralStringList.append(letters)  
    return (getRomanNumeralString(number, currentBasePower - 1, romanNumeralStringList) if (currentBasePower > 0) else
        ("".join(romanNumeralStringList)))

class Solution:
    def intToRoman(self, number: int) -> str:
        stringList = []
        currentBasePower = 3
        return getRomanNumeralString(number, currentBasePower, stringList)
