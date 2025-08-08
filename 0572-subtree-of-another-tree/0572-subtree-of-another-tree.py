# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        if root.val == subRoot.val:
            is_same_tree = self._checkSameTree(root, subRoot)
            if is_same_tree:
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def _checkSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        
        if root is None or subRoot is None:
            return False
        
        if root.val != subRoot.val:
            return False
        
        return self._checkSameTree(root.left, subRoot.left) and self._checkSameTree(root.right, subRoot.right)
        

        
        