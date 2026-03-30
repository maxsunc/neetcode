# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # in a tree there is only 1 unique path for each node

        # somehow keep track of previously max values 

        # root is always a good node
        # dfs but kee ptrack of the max value
        # automatically the root node is the max value

        res = 0

        def dfs(node, curMax):
            nonlocal res
            if node.val >= curMax:
                # update the max value
                curMax = node.val
                res = res + 1
            # call dfs from this curNode on let and right with the curMax Value
            if node.right:
                dfs(node.right, curMax)
            if node.left:
                dfs(node.left, curMax)


        dfs(root, -101)
        return res