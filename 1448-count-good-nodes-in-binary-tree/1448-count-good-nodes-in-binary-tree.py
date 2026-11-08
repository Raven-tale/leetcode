# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0

        def traverse(node, path_max):
            if node == None:
                return
            if node.val >= path_max:
                path_max = node.val
                self.good_nodes += 1
            traverse(node.left, path_max)
            traverse(node.right, path_max)
        
        traverse(root, root.val)
        return self.good_nodes
"""
Iterative or Recursive? I think iterative
Looks like BFS, check while traversing
O(n) for sure
Store values of maximum in layer

BFS Solution; Followed solution
Define self.variable
Helper function
"""