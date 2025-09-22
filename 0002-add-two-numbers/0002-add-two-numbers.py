class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # We'll iterate though the both linked-list to solve this problem.
        # We need to careful carry up digits when more nine digits.
        
        # Initialize linked list to track on head point
        head = ListNode()
        tail = head
        
        # Iterate thought the list and initialize valuable to track carry out
        carry_up = 0
        while carry_up or l1 or l2:
            v1_value = l1.val if l1 else 0
            v2_value = l2.val if l2 else 0
            
            total = v1_value + v2_value + carry_up
            
            # update digit and carry out
            carry_up, digit = divmod(total, 10)
            tail.next = ListNode(digit)
            tail = tail.next
            
            # the linked list moves step
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # this approach O(n+m) time and O(n+m) extra spaces complexity
        return head.next