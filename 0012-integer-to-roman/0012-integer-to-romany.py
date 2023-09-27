# 12. Integer to Roman
# Author: Kevin Zhao
# Time Complexity: O(1)
# Space Complexity: O(1)

from collections import OrderedDict

def generateNumberLists(singleDigitString : str, fiveDigitString : str, tenDigitString) -> List[str]:
    return []

NUMBER_POWER_TO_LETTER_LISTS = OrderedDict([
    (1, ["","I","II","III","IV","V","VI","VII","VIII","IX"]),
    (10, ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]),
    (100, ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]),
    (1000, ["","M","MM","MMM"])
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
        
