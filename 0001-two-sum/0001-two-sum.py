# 1. Two Sum
# Author: Kevin Zhao
# Time Complexity: O(n)
# Space Complexity: O(n)
# We intend to find (target - current_element) as long as the indicies

NOT_FOUND_RETURN_VALUE :  List[int] = []

def doesNonUniqueElementExist(elementToIndiciesDict : dict[int, list[int]], elementIndexTuple : tuple[int, int]) -> bool:
    element : int = elementIndexTuple[0]
    index : int =  elementIndexTuple[1]
    
    if element not in elementToIndiciesDict:
        return False
    
    indiciesSet = elementToIndiciesDict[element] 
    if (index in indiciesSet) and (len(indiciesSet) <= 1) :
        return False

    return True

def addElementToElementToIndiciesDict(elementToIndiciesDict : dict[int, list[int]], elementIndexTuple : tuple[int, int]) -> None:
    element = elementIndexTuple[0]
    index = elementIndexTuple[1]
    if element in elementToIndiciesDict:
        elementToIndiciesDict[element].append(index)
    else:
        elementToIndiciesDict[element] = [index]
    return None

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        elementToIndiciesDict : Dict[int, list[int]] = {}

        for index, element in enumerate(numbers):
            targetAddend = target - element
            if doesNonUniqueElementExist(elementToIndiciesDict, (targetAddend, index)):
                return [elementToIndiciesDict[targetAddend][0], index]

            addElementToElementToIndiciesDict(elementToIndiciesDict, (element, index))
        
        return INVALID_RETURN_VALUE
