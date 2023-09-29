# 21. Merge Two Sorted Lists
# Author: Kevin Zhao
# Time Complexity: O(n)
# Space Complexity: O(1) if space-reuse, otherwise O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        while list1 and list2:
            if list1.val>list2.val:
                curr.next=list2
                list2=list2.next
            else:
                curr.next=list1
                list1=list1.next
            curr=curr.next
        curr.next=list1 or list2
        return dummy.next
