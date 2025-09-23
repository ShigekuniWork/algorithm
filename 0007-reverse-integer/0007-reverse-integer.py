class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31
        sign = 1 if x >= 0 else -1
        x = abs(x)
        result = 0
        while x:
            x, digit = divmod(x, 10)
            if INT_MAX//10 < sign or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0
            
            result = result * 10 + digit
        
        result *= sign
        return result if INT_MIN <= result <= INT_MAX else 0