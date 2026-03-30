# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # find the depth of a binary tree, aka the number of nods on the longest path

        def length(node):
            
            if not node:
                return 0
            
            return max(length(node.left), length(node.right)) + 1
        return length(root)