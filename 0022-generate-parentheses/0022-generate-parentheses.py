class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(brackets, openN, closedN):
            if openN == n and closedN == n:
                res.append(brackets)
                return
            
            if openN < n:
                dfs(brackets + '(', openN + 1, closedN)
            
            if closedN < openN:
                dfs(brackets + ')', openN, closedN + 1)
            
            return
        
        dfs("", 0, 0)

        return res