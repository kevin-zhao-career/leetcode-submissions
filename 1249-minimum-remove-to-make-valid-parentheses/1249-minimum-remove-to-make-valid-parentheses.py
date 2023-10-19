# 1249. Minimum Remove to Make Valid Parentheses
# Author: Kevin Zhao
# Time Complexity: O(n)
# Space Complexity: O(1) if we reuse space, otherwise O(n)
# The idea is if ever goes negative, we should remove all the parenthesis, where each ")" is a -1 and each ")" is a positive

LEFT_PARENTHESIS = "("
RIGHT_PARENTHESIS = ")"

def isParenthesis(character : str) -> bool:
    if (len(character) != 1):
        return False
    return (character is LEFT_PARENTHESIS) or (character is RIGHT_PARENTHESIS)

def getScore(character : str) -> int:
    if not iSParenthesis(character):
        return 0
    return (1 if character is LEFT_PARENTHESIS else -1)

class Solution:
    def minRemoveToMakeValid(self, string: str) -> str:
        validParenthesisStringArray = []

        parenthesisScore = 0
        writeIndex = 0
        for readIndex, character in enumerate(string):
            additionalScore = getScore(character)
            if (parenthesisScore == 0) and (additionalScore < 0):
                continue

            string[writeIndex] = string[readIndex]
            parenthesisScore += additionalScore

        return string
