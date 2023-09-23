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
DEFAULT_CARRY : int = 0
BASE : int = 10

def getNextNode(node : Optional[ListNode]) -> Optional[ListNode]:
    return (None if (node is None) else node.next)

def getNextNodePair(nodePair : Tuple[Optional[ListNode], Optional[ListNode]]) -> Tuple[Optional[ListNode], Optional[ListNode]]:
    return (getNextNode(nodePair[0]), getNextNode(nodePair[1]))

def getNextNodes(nodePair : Tuple[Optional[ListNode], Optional[ListNode]], node: Optional[ListNode]) -> Tuple[Tuple[Optional[ListNode], Optional[ListNode]], Optional[ListNode]]:
    return (getNextNodePair(nodePair), node.next if (node is not None) else None)

def hasNextNode(node : Optional[ListNode]) -> bool:
    return (node is not None) and (node.next is not None)

def hasNextNodes(nodePair : Tuple[Optional[ListNode], Optional[ListNode]]) -> bool:
    return hasNextNode(nodePair[0]) or hasNextNode(nodePair[1])

def getValue(node : Optional[ListNode]) -> int:
    return node.val if (node is not None) else DEFAULT_VALUE

def getCarry(number : int, base : int) -> int:
    return (number / base)

def getRemainder(number : int, base : int) -> int:
    return (number % base)

def addNumbers(node1 : Optional[ListNode], node2 : Optional[ListNode], carry : int, reuseExistingData : bool) -> Tuple[Optional[ListNode], int]:
    if ((node1 is None) and (node2 is None) and (carry == 0)):
        return (None, DEFAULT_CARRY)

    number = sum([getValue(node1), getValue(node2), carry])
    nextCarry = getCarry(number, BASE)
    remainder = getRemainder(number, BASE)
    return (ListNode(remainder), nextCarry)

def addTwoNumbers(digitList1: Optional[ListNode], digitList2: Optional[ListNode], reuseExistingData : bool) -> Optional[ListNode]:
    nodePair = (digitList1, digitList2)
    beginNode = endNode = None
    carry : int = DEFAULT_CARRY

    while (hasNextNodes(nodePair)):
        if endNode is None:
            (endNode, carry) = addNumbers(nodePair[0], nodePair[1], carry, reuseExistingData)
        else:
            (endNode.next, carry) = addNumbers(nodePair[0], nodePair[1], carry, reuseExistingData)

        if beginNode is None:
            beginNode = endNode

        (nodePair, endNode) = getNextNodes(nodePair, endNode)

    return beginNode 

class Solution:
    def addTwoNumbers(self, digitList1: Optional[ListNode], digitList2: Optional[ListNode]) -> Optional[ListNode]:
        reuseExistingData = False
        return addTwoNumbers(digitList1, digitList2, reuseExistingData)
