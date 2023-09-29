# 21. Merge Two Sorted Lists
# Author: Kevin Zhao
# Time Complexity: O(n)
# Space Complexity: O(1) if space-reuse, otherwise O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def getBothNodesExist(list1Node: Optional[ListNode], list2Node: Optional[ListNode]) -> bool:
    return (list1Node is not None) and (list2Node is not None)

def hasNextNode(list1Node: Optional[ListNode], list2Node: Optional[ListNode]) -> bool:
    return (list1Node is not None) or (list2Node is not None)

def getNextNode(list1Node: Optional[ListNode], list2Node: Optional[ListNode]) -> Optional[ListNode]:
    return list1Node if ((list2Node is None) or (list2Node.val > list1Node.val)) else list2Node

def advanceNodes(list1Node: Optional[ListNode], list2Node: Optional[ListNode]) -> Tuple[Optional[ListNode], Optional[ListNode]]:
    bothNodesExist = getBothNodesExist(list1Node, list2Node)
    list1NodeLessThanList2Node = (bothNodesExist) and (list1Node.val < list2Node.val)
    list1NodeNext = list1Node.next if list1NodeLessThanList2Node else list1Node
    list2NodeNext = list2Node.next if (not list1NodeLessThanList2Node) else list2Node
    return (list1NodeNext, list2NodeNext)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            return list1 if (list2 is None) else list2
        beginNode = None
        currentNode = None
        
        while hasNextNode(list1, list2):
            currentNode = getNextNode(list1Node, list2Node)
            (list1, list2) = advanceNodes(list1, list2)
        return beginNode
