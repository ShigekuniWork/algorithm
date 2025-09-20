from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # I will solve this with DFS in a bottom-up way.
        # At each node, I check the height of the left side and the right side.
        # If the gap is bigger than one, that subtree is not balanced.

        def checkHeight(node: Optional[TreeNode]) -> int:
            # If the node is None, the height is zero.
            if node is None:
                return 0

            # First I check the left side. If it is unbalanced, I pass up -1.
            left_height = checkHeight(node.left)
            if left_height == -1:
                return -1

            # Then I check the right side. If it is unbalanced, I pass up -1.
            right_height = checkHeight(node.right)
            if right_height == -1:
                return -1

            # If the difference between left and right is more than one, return -1.
            if abs(left_height - right_height) > 1:
                return -1

            # Otherwise, the height here is max of left and right plus one.
            return max(left_height, right_height) + 1

        # The tree is balanced if the helper does not return -1.
        return checkHeight(root) != -1

        # Time is O(n) because I visit each node once.
        # Space is O(h) for the call stack, where h is the height of the tree.
