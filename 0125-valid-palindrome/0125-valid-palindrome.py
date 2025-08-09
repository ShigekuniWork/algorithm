class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = [c.casefold() for c in s if c.isalnum()]
        return t == t[::-1]



                
                
