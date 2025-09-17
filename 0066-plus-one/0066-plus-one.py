from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # I will simulate addition starting from the last digit.
        # If the digit is 9, set it to 0 and carry over to the next digit on the left.
        # If all digits are 9, we create a new leading 1.
        # This algorithm runs in O(N) time.
        # For space complexity, it is O(1) in the common case since we modify the input list in place.
        # But in the worst case, when all digits are 9, we create a new array, so it takes O(N) extra space

        index = len(digits) - 1

        # Propagate carry while digits are 9.
        while index >= 0 and digits[index] == 9:
            digits[index] = 0
            index -= 1

        # If index < 0, it means all digits were 9.
        if index < 0:
            return [1] + digits

        # Otherwise, just increment the current digit.
        digits[index] += 1
        return digits
