class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We use a sliding window with two pointers.
        # We keep the last index for each char so we can jump the left side fast.

        seen = {}
        left = 0
        best = 0

        for right in range(len(s)):
            c = s[right]

            # If c was seen inside the window, we move left past that index.
            if c in seen and seen[c] >= left:
                left = seen[c] + 1

            # We update the last index of c.
            seen[c] = right

            # We update the best length if this window is longer.
            best = max(best, right - left + 1)

        # Time is O(n) because each index moves at most once.
        # Space is O(min(n, k)) for the map, where k is the charset size.
        return best
