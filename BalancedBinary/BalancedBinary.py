# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def isBalanced(self, root: Optional['TreeNode']) -> bool:
        def check(node):
            # Base case: empty tree has height 0 (balanced)
            if not node:
                return 0

            # Recursively check left and right subtrees
            left_height = check(node.left)
            right_height = check(node.right)

            # If either subtree is already unbalanced, bubble up -1
            if left_height == -1 or right_height == -1:
                return -1

            # If height difference > 1, this node is unbalanced
            if abs(left_height - right_height) > 1:
                return -1

            # Otherwise, return the height of this subtree
            return 1 + max(left_height, right_height)

        # Tree is balanced if we never saw -1
        return check(root) != -1
