# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # find the lowest common ancestor of a binary tree.

        # the top node is guarunteed to be an ancestor.

        # if the value is in left (or this is the value) and the value is in right (or this is hte value)
        # then we can return true


        # what should we return if it is empty
        # is it possible for q to be equal to p
        # use dfs: 
        res = (0, root)  # take the higher level
        def dfs(curNode, level):
            nonlocal res
            if not curNode:
                return (False,False)
            stat = (curNode == q, curNode == p)
            leftTree = dfs(curNode.left, level + 1)
            rightTree = dfs(curNode.right, level + 1)
            stat = (stat[0] or leftTree[0] or rightTree[0], stat[1] or leftTree[1] or rightTree[1])
            if stat[0] and stat[1]:
                if level > res[0]:
                    res = (level, curNode)
            return stat
        dfs(root, 0)
        return res[1]

