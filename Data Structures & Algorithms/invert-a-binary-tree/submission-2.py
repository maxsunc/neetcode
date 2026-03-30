# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # inverting a binary tree

        def invert(node):
            if not node:
                return
            # swap the left and right and call invert on left and right
            print(f"reversing at {node.val}")
            left = node.left
            node.left = node.right
            node.right = left
            
            if node.left:
                invert(node.left)
            if node.right:
                invert(node.right)
            return
        
        invert(root)

        return root
        