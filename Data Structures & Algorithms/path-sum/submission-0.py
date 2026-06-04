# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # does it have a root to leaf path such that adding up all those values equals target sum

        # we'll have to try all possible combos if there are negative values

        # recursive dfs

        # base case is when we cant explore right or left then we just check and see if the sum is matching if it is return True
        # if not return false

        # recursive case if left or right returns true then return True as well, then default to false if not

        def dfs(curNode, curSum):
            if not curNode:
                return False
            curSum += curNode.val
            if not curNode.left and not curNode.right:
                # at a leaf node
                return targetSum == curSum

            if curNode.left:
                # explore left if possible
                if dfs(curNode.left, curSum):
                    return True
            if curNode.right:
                if dfs(curNode.right,curSum):
                    return True
            
            # default to return False
            return False
        # only call dfs if root isn't none
        return dfs(root,0)