class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        I'll approach this problem by using a sliding window.
        I'll iterate through the string and store each character in a hash map while updating the result.
        If the current character is already in the hash map, I'll move the left pointer forward 
        to the position after the previous occurrence. 
        """
        # Initialize hash map, left pointer, and response
        mp = {}
        left = 0
        response = 0

        # Iterate through the string using index as right pointer
        for right in range(len(s)):
            # Check whether the current character has been seen before
            if s[right] in mp:
                # If so, update left pointer to skip the duplicate
                left = max(mp[s[right]] + 1, left)
            
            # Store the current character's index in hash map
            mp[s[right]] = right
            # Update the maximum length
            response = max(response, right - left + 1)
        
        return response
        """
        Time complexity is O(n) because this approach uses a single loop.
        Space complexity is O(n) because this approach uses a hash map to store seen characters.
        """