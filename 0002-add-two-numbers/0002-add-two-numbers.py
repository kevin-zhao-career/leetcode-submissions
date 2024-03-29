# 2. Add Two Numbers
# Author: Kevin Zhao
# Time Complexity: O(n)
# Space Complexity: O(1) if datastructure is being reused otherwise O(n)

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

def hasNode(node : Optional[ListNode]) -> bool:
    return (node is not None)

def hasNodes(nodePair : Tuple[Optional[ListNode], Optional[ListNode]], carry:int) -> bool:
    return hasNode(nodePair[0]) or hasNode(nodePair[1]) or (carry > 0)

def getValue(node : Optional[ListNode]) -> int:
    return node.val if (node is not None) else DEFAULT_VALUE

def getCarry(number : int, base : int) -> int:
    return int(number / base)

def getRemainder(number : int, base : int) -> int:
    return (number % base)

def getListNode(node1 : Optional[ListNode], node2 : Optional[ListNode], remainder: int, reuseExistingData : bool) -> Optional[ListNode]:
    if (not reuseExistingData) or ((node1 is None) and (node2 is None)):
        return ListNode(remainder)
    
    if (node1 is not None):
        node1.val = remainder
    else:
        node2.val = remainder

    return node1 if (node1 is not None) else node2

def addNumbers(node1 : Optional[ListNode], node2 : Optional[ListNode], carry : int, reuseExistingData : bool) -> Tuple[Optional[ListNode], int]:
    if ((node1 is None) and (node2 is None) and (carry == 0)):
        return (None, DEFAULT_CARRY)

    number = sum([getValue(node1), getValue(node2), carry])
    nextCarry = getCarry(number, BASE)
    remainder = getRemainder(number, BASE)
    return (getListNode(node1, node2, remainder, reuseExistingData), nextCarry)

def addTwoNumbers(digitList1: Optional[ListNode], digitList2: Optional[ListNode], reuseExistingData : bool) -> Optional[ListNode]:
    if (reuseExistingData) and ((digitList1 is None) or (digitList2 is None)):
        return (digitList1 if (digitList2 is None) else digitList2)

    nodePair = (digitList1, digitList2)
    beginNode = endNode = None
    carry : int = DEFAULT_CARRY

    while (hasNodes(nodePair, carry)):
        if endNode is None:
            (endNode, carry) = addNumbers(nodePair[0], nodePair[1], carry, reuseExistingData)
        else:
            (endNode.next, carry) = addNumbers(nodePair[0], nodePair[1], carry, reuseExistingData)
            endNode = endNode.next

        if beginNode is None:
            beginNode = endNode

        nodePair = getNextNodePair(nodePair)
    
    return beginNode

class Solution:
    def addTwoNumbers(self, digitList1: Optional[ListNode], digitList2: Optional[ListNode]) -> Optional[ListNode]:
        reuseExistingData = True
        return addTwoNumbers(digitList1, digitList2, reuseExistingData)
