class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # We add the numbers digit by digit with a running carry.
        # The loop reads one node from each list, adds them with the carry, and writes one digit.
        # If the sum goes over nine, the carry moves to the next round.

        # It keeps the start of the result list.
        dummy = ListNode()
        tail = dummy

        # We carry as an integer to keep the math simple.
        carry = 0

        # The loop runs while any digit or a carry remains.
        while l1 or l2 or carry:
            # It reads the current digits; missing nodes act like zero.
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0

            # It adds both digits and the carry.
            total = l1_value + l2_value + carry

            # It writes the ones place and updates the carry.
            carry, digit = divmod(total, 10)
            tail.next = ListNode(digit)
            tail = tail.next

            # The pointers move forward when possible.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Time is O(n + m) because the loop touches each node once.
        # Space is O(n + m) for the new list, excluding input lists.
        return dummy.next
