# 12. Integer to Roman
# Author: Kevin Zhao
# Time Complexity: O(1)
# Space Complexity: O(1)

from collections import OrderedDict

def generateNumberLists(singleDigitString : str, fiveDigitString : str, tenDigitString) -> List[str]:
    numberList = []
    for number in range(0, 10):
        if number == 9:
            numberList.append(singleDigitString + tenDigitString)
        elif number == 4:
            numberList.append(singleDigitString + fiveDigitString)
        elif number >= 5:
            numberList.append(fiveDigitString + (singleDigitString * (number - 5)))
        else:
            numberList.append(singleDigitString * number) 
    return numberList

NUMBER_POWER_TO_LETTER_LISTS = OrderedDict([
    (1, generateNumberLists("I", "V", "X")),
    (10, generateNumberLists("X", "L", "C")),
    (100, generateNumberLists("C", "D", "M")),
    (1000, generateNumberLists("M", "5M", "10M"))
])

def getDigit(number : int, currentPower : int) -> int:
    return int((number % (currentPower * 10)) / currentPower)

class Solution:
    def intToRoman(self, number: int) -> str:
        stringList = []
        currentPower = 1000
        while (currentPower > 0):
            letterList = NUMBER_POWER_TO_LETTER_LISTS[currentPower]
            digit = getDigit(number, currentPower)
            letters = letterList[digit]
            stringList.append(letters)
            currentPower /= 10
            currentPower = int(currentPower)
        return "".join(stringList)
        
