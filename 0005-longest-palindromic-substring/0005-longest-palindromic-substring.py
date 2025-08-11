class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        start, end = 0, 0

        for i in range(n):
            # 奇数長
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l > end - start:
                    start, end = l, r
                l -= 1
                r += 1

            # 偶数長
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l > end - start:
                    start, end = l, r
                l -= 1
                r += 1

        return s[start:end+1]

        