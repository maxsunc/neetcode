# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # length of the longest path between any two nodes within that tree

        # path doesn ot have to pass throug the root
        # 1 traversal

        # return 0 if one node?
        # return -1 if no node?
        

        # brute force solution:
        # for each node compute the longest path
        # to computer the longest path we do 1 + height(left) + height(right)

        # for each node do that
        res = 0


        def dfs(curNode):
            if not curNode:
                return 0
            nonlocal res
            # the function dfs returns the highest height from left and right and checks whether the diameter of that node
            # is big enough to replace res
            leftHeight, rightHeight = dfs(curNode.left), dfs(curNode.right)
            if leftHeight + rightHeight > res:
                res = leftHeight + rightHeight
            
            # return the height at this node
            return max(leftHeight, rightHeight) + 1
        
        dfs(root)
        return res
            
            


