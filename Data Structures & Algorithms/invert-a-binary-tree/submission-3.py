# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Simple: INvert a binary tree by flipping the left and right children of each node

        # do we just reutrn empty if its nothing?
        # is the input case always valid?
        # are we looking for time or space complexity

        # swap the right and left node then recursively call to invert the binary tree of the left and right nodes if it exists
        # 
        def invert(node):
            if not node:
                return
            # flip the left and irght
            tmp = node.left
            node.left = node.right
            node.right = tmp

            # call invert on left and right
            invert(node.left)
            invert(node.right)
        invert(root)
        return root