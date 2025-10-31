# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {v: i for i, v in enumerate(inorder)}
        
        self.pre_idx = 0
        def dfs(left: int , right: int):
            if left > right:
                return
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root
        
        return dfs(0, len(preorder) -1)

        