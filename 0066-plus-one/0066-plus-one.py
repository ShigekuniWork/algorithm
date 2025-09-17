from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # I will simulate addition from the last digit to the first.
        # Iterate backwards: if the digit is less than 9, increment and return.
        # If the digit is 9, set it to 0 and continue carrying over.
        # If all digits are 9, prepend a new 1 at the front.
        # This runs in O(N) time and in the worst case O(N) extra space.

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # If we finish the loop, all digits were 9.
        return [1] + digits
