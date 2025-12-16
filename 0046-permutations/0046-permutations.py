class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        def dfs(curr):
            if len(curr) == n:
                res.append(curr.copy())
                return
            for x in nums:
                if x in curr:
                    continue
                curr.append(x)
                dfs(curr)
                curr.pop()

        dfs([])
        return res
