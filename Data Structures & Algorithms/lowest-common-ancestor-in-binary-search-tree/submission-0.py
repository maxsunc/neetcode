# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # since we're guarunteed that p and q exist withi n hte tree
        # traversal cases:
        if p.val > root.val and q.val > root.val:
            # move to the right
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            # they're split
            # we kmnow that this is the lowest common ancestor
            return root