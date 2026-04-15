# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # value is less than or equal to both p.val and q.val?

        # gbinary search tree menas everything to the right is bigger than us and everything to the left is smaller than us
        # we're guarunteed to have a valid bst

        # the root should be guarunteed to be an ancestor?

        # if the nodes are split (both on a different side then we can't go any further and have found the lowest common ancestor)
        # to check if they've split check whether curNode.val >= one val and <= another Val

        def findLCA(node):
            if not node:
                return None
            
            # if both values are less than the value then explore the left tree for a new ancesotr
            if node.val > p.val and node.val > q.val:
                return findLCA(node.left)
            elif node.val < p.val and node.val < q.val:
                return findLCA(node.right)
            else:
                # its in between so just return the node since we know this is hte LCA
                return node
        return findLCA(root)
        

