#!/bin/python

from typing import Final

SINGLE_WILDCARD: Final[str] = '.'
MULTIPLE_WILDCARD: Final[str] = '*'   

def getInitialTable(rowSize: int, columnSize: int):
    if (rowSize == 0) or (columnSize == 0):
        return []

    initialTable = [[False] * (columnSize + 1) for _ in range(rowSize + 1)]
    initialTable[0][0] = True
    return initialTable

class Solution:
    def isMatch(self, inputString: str, patternMatch: str) -> bool:
        inputStringLength = len(inputString)
        patternMatchLength = len(patternMatch)

        regularExpressionMatchingTable = getInitialTable(inputStringLength, patternMatchLength)

        for patternMatchIndex in range(1, patternMatchLength+1):
            if patternMatch[patternMatchIndex-1] == MULTIPLE_WILDCARD:
                regularExpressionMatchingTable[0][patternMatchIndex] = regularExpressionMatchingTable[0][patternMatchIndex-2]
            else:
                regularExpressionMatchingTable[0][patternMatchIndex] = (patternMatchIndex > 1 and patternMatch[patternMatchIndex-2] == MULTIPLE_WILDCARD and regularExpressionMatchingTable[0][patternMatchIndex-2])


        for inputStringLength in range(1, inputStringLength+1):
            for patternMatchLength in range(1, patternMatchLength+1):
                if patternMatch[patternMatchLength-1] == inputString[inputStringLength-1] or patternMatch[patternMatchLength-1] == SINGLE_WILDCARD:
                    regularExpressionMatchingTable[inputStringLength][patternMatchLength] = regularExpressionMatchingTable[inputStringLength-1][patternMatchLength-1]
                elif patternMatch[patternMatchLength-1] == MULTIPLE_WILDCARD:
                    regularExpressionMatchingTable[inputStringLength][patternMatchLength] = regularExpressionMatchingTable[inputStringLength][patternMatchLength-2] or (patternMatch[patternMatchLength-2] == inputString[inputStringLength-1] or patternMatch[patternMatchLength-2] == SINGLE_WILDCARD) and regularExpressionMatchingTable[inputStringLength-1][patternMatchLength]
                else:
                    regularExpressionMatchingTable[inputStringLength][patternMatchLength] = False

        return regularExpressionMatchingTable[inputStringLength][patternMatchLength]

        
