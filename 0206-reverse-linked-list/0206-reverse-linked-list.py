# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummey = ListNode()

        while head:
            curr_last = dummey.next
            dummey.next = ListNode(head.val)
            dummey.next.next = curr_last

            head = head.next
        
        return dummey.next
        