from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # I will use an iterative merge with a dummy node.
        # Maintain a tail pointer to build the merged list in place.
        # While both lists are non-empty, compare their heads and append the smaller node.
        # After the loop, append the remaining nodes from whichever list is not empty.
        # This runs in O(m + n) time and O(1) extra space.

        dummy = ListNode()
        tail = dummy

        # Merge while both lists have nodes.
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Append the remainder.
        tail.next = list1 if list1 else list2

        # Return the head of the merged list.
        return dummy.next
