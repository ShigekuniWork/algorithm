class Solution:
    def countSubstrings(self, s: str) -> int:
        response = 0

        def count_palindrome(s, left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            return count
        
        for i in range(len(s)):
            response += count_palindrome(s, i, i)
            response += count_palindrome(s, i, i + 1)
        
        return response
