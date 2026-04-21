# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # determine is it a valid bst?
        # left node is strictly less than node's key
        # right node is strictly greater than node's key

        # when we go to the left 

        if not root:
            return True

        # repeat check for both left and right
        
        def dfs(curNode, lowest, highest):
            # update the lowest and highest
            # need to keep track of the lowest and highest value seen and pass that trhu
            if curNode.left:
                # check whether left is strictly less than us
                if curNode.left.val >= curNode.val or lowest >= curNode.left.val:
                    return False
                # check dfs onto the left node
                if not dfs(curNode.left, lowest, curNode.val):
                    return False
            
            if curNode.right:
                if curNode.right.val <= curNode.val or highest <= curNode.right.val:
                    # print("RIGHT IS WRONG")
                    return False
                if not dfs(curNode.right, curNode.val, highest):
                    return False
            return True
        return dfs(root,-math.inf,math.inf)