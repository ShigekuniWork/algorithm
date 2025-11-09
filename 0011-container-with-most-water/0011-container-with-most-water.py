class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        I'll approach this problem using two pointers.
        I'll assign the first index and last index to left and right pointers.
        Then I'll iterate through the heights list, comparing the values at left and right pointers.
        I'll move the pointer with the smaller height to the next position and compare the result with the current maximum. 
        """
        # Assign first index and last index to left, right
        left = 0
        right = len(heights) - 1

        # Assign 0 to result
        result = 0

        # Loop starts while left index less than right index
        while left < right:
            # Calculate current maximum amount of water
            amount = min(heights[left], heights[right]) * (right - left)

            # Compare current amount with the current result
            result = max(result, amount)

            # Move the pointer with the smaller height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return result
        """
        Time complexity is O(n) because this approach uses a single loop only.
        Space complexity is O(1)
        """