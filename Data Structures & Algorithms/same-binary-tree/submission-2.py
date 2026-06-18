# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # dfs problem

        def dfs(curNode1, curNode2):
            if not curNode1 and not curNode2:
                return True
            if (curNode1 and not curNode2) or (not curNode1 and curNode2):
                return False
            if curNode1.val != curNode2.val:
                return False
            if not dfs(curNode1.left, curNode2.left):
                return False
        
            if not dfs(curNode1.right,curNode2.right):
                return False
            return True


        return dfs(p, q)