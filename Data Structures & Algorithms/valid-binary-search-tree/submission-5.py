# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # valid bst?
        # simple: see if a tree is a valid bst or not:
        # the left subtree of a node contains only nodes with key
        # the right subtree of a node contains only nodes greater than that

        #    5
        #   1 6
        #    4
        #-1 2
        # dfs traversal
        # curNode, minValue, maxValue

        # when we go to the left update maxValue if needed
        # check if value is between minVal and maxVal
        
        # everytime we go left: updateMaxvalue to maxValue = min(maxValue, curVal)
        # everytime we go right: minvalue = max(minValue, curVal
        
        # 
        def dfs(curNode, minValue,maxValue):
            if not curNode:
                return True
            if not (minValue < curNode.val and curNode.val < maxValue):
                return False
            
            return dfs(curNode.left, minValue, min(maxValue, curNode.val)) and dfs(curNode.right, max(minValue,curNode.val), maxValue)
        return dfs(root, -math.inf,math.inf)