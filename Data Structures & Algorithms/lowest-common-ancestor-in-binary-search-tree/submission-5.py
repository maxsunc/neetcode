# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            # simple: We want to find the lowest common ancestor of a bst
            # bst property: the vlaues of left are less than the values or right
            
            # we just wanna find the point where its split
            # if the curNode is in between p and q then return it
            if (p.val <= root.val and root.val <= q.val) or (q.val <= root.val and root.val <= p.val):
                return root
            
            # its not in between, either both are less than root (left) or both are greater than root (right)
            if p.val >= root.val and q.val >= root.val:
                return self.lowestCommonAncestor(root.right,p,q)
            return self.lowestCommonAncestor(root.left,p,q)