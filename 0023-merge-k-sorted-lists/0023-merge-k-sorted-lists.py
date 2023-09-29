# 23. Merge k Sorted Lists
# Author: Kevin Zhao
# Time Complexity: O(n log k)
# Space Complexity: O(k)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)                 # creating a garbage node whose location we will always know and the sorted list will be appended from here
        heap = []

        for n in lists:                      # run for number of linked lists times i.e. [[A], [B], [C]]
            while n:                         # run for number of elements in a particular LL times i.e. [x, y, z]
                heapq.heappush(heap, n.val)  # In heap using Heap-Queue property insert the value n, such that the heap remains sorted in ascending order
                n = n.next

        cur = dummy                          # we take a current pointer to point at the dummy node, so we can append our sorted LL
        while heap:
            temp = ListNode(heapq.heappop(heap))  # converting the heap into Node(val,nxt) one by one
            cur.next = temp                       # dummy(cur) -> Node1[val]
            cur = cur.next                        # dummy -> Node1[val](cur)
        cur.next = None                           # dummy -> Node1[val] -> Node1[val] -> Node1[val] -> Node1[val](cur) -> Null
        return dummy.next
