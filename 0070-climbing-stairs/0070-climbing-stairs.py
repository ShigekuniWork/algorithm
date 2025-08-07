class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        prev = 1
        curr = 2

        for _ in range(3, n+1):
            next = prev + curr
            prev = curr
            curr = next
        
        return curr
