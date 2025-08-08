# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        cache = []

        while head is not None:
            if head in cache:
                # cycle node
                return True
            cache.append(head)
            head = head.next

        return False