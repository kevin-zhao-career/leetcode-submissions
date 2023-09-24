# 3. Longest Substring Without Repeating Characters
# Author: Kevin Zhao
# Time Complexity: O(n)
# Space Complexity: O(1) since there are at most a constant number of characters
MAXIMUM_LIMIT = 26
def getUpdatedCurrentSubstringBeginIndex(characterToIndexDict, character, currentSubstringBeginIndex):
    return ((characterToIndexDict[character] + 1) if ((characterToIndexDict[character] + 1) > currentSubstringBeginIndex)
                else (currentSubstringBeginIndex))


class Solution:
    def lengthOfLongestSubstring(self, sentence: str) -> int:
        maximumNonrepeatingSubstringLength = 0
        characterToIndexDict = {}

        currentSubstringBeginIndex = 0
        for index, character in enumerate(sentence):
            if (character in characterToIndexDict):
                currentSubstringBeginIndex = getUpdatedCurrentSubstringBeginIndex(characterToIndexDict, character, currentSubstringBeginIndex)
            
            characterToIndexDict[character] = index
            maximumNonrepeatingSubstringLength = max(maximumNonrepeatingSubstringLength,
                index - currentSubstringBeginIndex + 1)

        return maximumNonrepeatingSubstringLength
        
