class Solution:
    def climbStairs(self, n: int) -> int:
        curr, prev = 1, 1

        for _ in range(n - 1):
            temp = curr
            curr += prev
            prev = temp
        
        return curr