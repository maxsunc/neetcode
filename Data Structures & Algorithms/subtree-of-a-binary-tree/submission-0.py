# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            # traversing root
            # calling isSameTree on each node we come across
        if self.isSameTree(root, subRoot):
            return True
        if root:
        # recursive case:
            return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)
        return False


    def isSameTree(self, node1, node2):
        # node1.val != node2.val
        if not node1 and not node2: # both are empty so we're good
            return True
        if (not node1 or not node2) or node1.val != node2.val:
            return False
        
        return self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right,node2.right)

