# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # I will solve this problem using recursion with a DFS approach.
        # The idea is to check the depth of the left side and the right side,
        # and then return the larger one.

        # If the root is None, that means we reached the end of a branch.
        # In that case, the depth is 0.
        if root is None:
            return 0

        # Recursively get the depth of left and right subtrees, and add 1 for the current node.
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1

        # Return the maximum of the two depths.
        return max(left, right)