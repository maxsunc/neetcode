# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # have a result of a list 
        # we want to find the rightmost node and add to the result
        # we should probably also track the level of the binary tree so that way we don't accidenatlly add extras

        # track the level of the binary tree we are at in our recursive function
        # rootnode is always added
        # dfsAdd(node, level)
        # it will try to go right first
        # left 2nd
        # it will skip if the len(res) > level
        # only add if len(res) == level

        # everytime we move down increase level
        res = []
        def dfs(node, level):
            if not node:
                return
            if len(res) == level:
                # valid so you can add it
                res.append(node.val)
            # check the right value first 
            dfs(node.right, level + 1)
            dfs(node.left,level + 1)
        
        dfs(root,0)
        return res
