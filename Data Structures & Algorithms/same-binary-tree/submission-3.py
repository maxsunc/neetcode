# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(curNode1,curNode2):
            if (not curNode1 and curNode2) or (curNode1 and not curNode2):
                return False 
            if not curNode1 and not curNode2:
                return True
            

            # both exist
            if curNode1.val != curNode2.val:
                return False
            
            return isSame(curNode1.left,curNode2.left) and isSame(curNode1.right,curNode2.right)
        
        return isSame(p,q)