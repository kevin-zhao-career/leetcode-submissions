# 3. Longest Substring Without Repeating Characters
# Author: Kevin Zhao
# Time Complexity: O(n)
# Space Complexity: O(1) since there are at most a constant number of characters
MAXIMUM_LIMIT = 26

class Solution:
    def lengthOfLongestSubstring(self, sentence: str) -> int:
        maximumNonrepeatingSubstringLength = 0
        characterToIndexDict = {}

        currentSubstringBeginIndex = 0
        for index, character in enumerate(sentence):
            if (character in characterToIndexDict) and (characterToIndexDict[character] + 1 > currentSubstringBeginIndex):
                currentSubstringBeginIndex = characterToIndexDict[character] + 1
            characterToIndexDict[character] = index

            maximumNonrepeatingSubstringLength = max(maximumNonrepeatingSubstringLength,
                index - currentSubstringBeginIndex + 1)

        return maximumNonrepeatingSubstringLength
        
