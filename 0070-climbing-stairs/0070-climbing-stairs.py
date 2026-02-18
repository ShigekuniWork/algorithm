class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        curr, prev = 1, 1

        for _ in range(n-1):
            curr, prev = curr + prev, curr

        return curr