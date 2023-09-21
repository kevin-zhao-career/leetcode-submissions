# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Breadth First Search
# Time Complexity: O(N)
# Space Complexity: O(N)

def getValue(node : TreeNode) -> int:
    return 0 if node is None else node.val

def getValues(currentLevelNodeToParentDict : dict[TreeNode, TreeNode]):
    return [currentLevelNode.val for currentLevelNode in currentLevelNodeToParentDict.keys()]

def setChildNodeToNone(parentNode : TreeNode, childNode : TreeNode):
    if parentNode is None:
        return
    
    if (parentNode.left is not None) and (getValue(parentNode.left) == getValue(childNode)):
        parentNode.left = None

    if (parentNode.right is not None) and (getValue(parentNode.right) == getValue(childNode)):
        parentNode.right = None

    return

def getNextLevelNodeToParentDict(currentLevelNodeToParentDict : dict[TreeNode, TreeNode]) -> Tuple[dict[TreeNode, TreeNode], bool]:
    foundInvalidNode = False
    nextLevelNodeToParentDict = {}

    for currentLevelNode, parentNode in currentLevelNodeToParentDict.items():
        if currentLevelNode.left is not None:
            nextLevelNodeToParentDict[currentLevelNode.left] = currentLevelNode

        invalidCandidate = currentLevelNode.right
        if invalidCandidate is None:
            continue

        nextLevelNodeToParentDict[invalidCandidate] = currentLevelNode

        if (invalidCandidate in currentLevelNodeToParentDict):
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
        while currentLevelNodeToParentDict:
            (currentLevelNodeToParentDict, foundInvalidNode) = getNextLevelNodeToParentDict(currentLevelNodeToParentDict)
            if foundInvalidNode:
                break

        return root
