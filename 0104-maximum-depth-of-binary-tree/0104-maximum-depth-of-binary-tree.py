# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        # If l and r no children
        if not root: return 0
        # Else find max of l, s
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
        """
        root can be None, is n == work
        Got algorithm, tree traversal based on max n
        Optimisations:
        == is slow
        Else not slow
        Trying moving recursion calls outside max function
        """
