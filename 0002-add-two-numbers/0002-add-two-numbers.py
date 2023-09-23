# 2. Add Two Numbers
# Author: Kevin Zhao
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

DEFAULT_VALUE : int = 0

def getNextNode(node : Optional[ListNode]) -> Optional[ListNode]:
    return (None if (node is None) else node.next)

def getNextNodes(nodePair : Tuple[Optional[ListNode], Optional[ListNode]]) -> Tuple[Optional[ListNode], Optional[ListNode]]:
    return (getNextNode(nodePair[0]), getNextNode(nodePair[1]))

def getNextNodes(nodePair : Tuple[Optional[ListNode], Optional[ListNode]], node: Optional[ListNode]) -> Tuple[Tuple[Optional[ListNode], Optional[ListNode]], optional[Node]:
    return (getNextNodes(nodePair), node.next if (node is not None) else None)

def hasNextNode(node : Optional[ListNode]) -> bool:
    return (node is not None) and (node.next is not None)

def hasNextNodes(nodePair : Tuple[Optional[ListNode], Optional[ListNode]]) -> bool:
    return hasNextNode(nodePair[0]) or hasNextNode(nodePair[1])

def getValue(node : ListNode) -> int:
    return node.val

def getValue(node : Optional[ListNode]) -> int:
    return getValue(node) if node is not None else DEFAULT_VALUE

def addNumbers(number1 : int, number2 : int, carry : int) -> int:
    return (number1 + number2 + number3)

def addTwoNumbers(node1 : ListNode, node2 : ListNode, carry : int, reuseExistingData : bool) -> Tuple[ListNode, int]:
    return False

def addTwoNumbers(digitList1: Optional[ListNode], digitList2: Optional[ListNode], reuseExistingData : bool) -> Optional[ListNode]):
    nodePair = (digitList1, digitList2)
    beginNode = endNode = None
    carry : int = 0

    while (hasNextNodes(nodePair)):
        (endNode.next, carry) = addTwoNumbers(nodePair[0], nodePair[1], carry, reuseExistingData)
        
        if beginNode is not None:
            beginNode = endNode

        (nodePair, endNode) = getNextNodes(nodePair, endNode)

    return beginNode 

class Solution:
    def addTwoNumbers(self, digitList1: Optional[ListNode], digitList2: Optional[ListNode]) -> Optional[ListNode]:
        reuseExistingData = False
        return addTwoNumbers(digitList1, digitList2, reuseExistingData)
