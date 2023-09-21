# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Breadth First Search
# Time Complexity: O(N)
# Space Complexity: O(N)

LEFT_CHILD_ATTRIBUTE_STRING : str = 'left'
RIGHT_CHILD_ATTRIBUTE_STRING : str = 'right'
CHILDREN_ATTRIBUTE_STRINGS : list[str] = [LEFT_CHILD_ATTRIBUTE_STRING, RIGHT_CHILD_ATTRIBUTE_STRING]

def getValue(node : TreeNode) -> int:
    return 0 if (node is None) else node.val

def getValues(currentLevelNodeToParentDict : dict[TreeNode, TreeNode]):
    return [currentLevelNode.val for currentLevelNode in currentLevelNodeToParentDict.keys()]

def setNodeToNoneIfValueEquivalent(parentNode : TreeNode, childNode : TreeNode, childAttributeString : str) -> None:
    if (parentNode is None) or (childNode is None):
        return

    if (getValue(getattr(parentNode, childAttributeString)) == getValue(childNode)):
        setattr(parentNode, childAttributeString, None)
    
    return

def setChildNodeToNone(parentNode : TreeNode, childNode : TreeNode) -> None:
    if parentNode is None:
        return

    for childrenAttributeString in CHILDREN_ATTRIBUTE_STRINGS:
        setNodeToNoneIfValueEquivalent(parentNode, childNode, childrenAttributeString)

    return

def addChildrenToLevelNodeToParentDict(levelNodeToParentDict : dict[TreeNode, TreeNode], node : TreeNode) -> None:
    if node is None:
        return

    for childrenAttributeString in CHILDREN_ATTRIBUTE_STRINGS:
        childNode = getattr(node, childrenAttributeString)
        if childNode is None:
            continue
        levelNodeToParentDict[childNode] = node
    return

def getNextLevelNodeToParentDict(currentLevelNodeToParentDict : dict[TreeNode, TreeNode]) -> Tuple[dict[TreeNode, TreeNode], bool]:
    foundInvalidNode = False
    nextLevelNodeToParentDict = {}

    for currentLevelNode, parentNode in currentLevelNodeToParentDict.items():
        addChildrenToLevelNodeToParentDict(nextLevelNodeToParentDict, currentLevelNode)

        invalidCandidate = currentLevelNode.right
        if (invalidCandidate not in currentLevelNodeToParentDict):
            continue
        
        foundInvalidNode = True
        parentNode = currentLevelNodeToParentDict[currentLevelNode]            
        setChildNodeToNone(parentNode, currentLevelNode)
        break

    return (nextLevelNodeToParentDict, foundInvalidNode)

class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        currentLevelNodeToParentDict = {root : None}
        while len(currentLevelNodeToParentDict):
            (currentLevelNodeToParentDict, foundInvalidNode) = getNextLevelNodeToParentDict(currentLevelNodeToParentDict)
            if foundInvalidNode:
                break

        return root
