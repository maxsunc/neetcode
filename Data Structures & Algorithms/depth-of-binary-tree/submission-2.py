# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # find the depth of a binary tree, aka the number of nods on the longest path

        # def length(node):
            
        #     if not node:
        #         return 0
            
        #     return max(length(node.left), length(node.right)) + 1
        # return length(root)

        # iteratively using dfs but iwth a stack
        stack = []
        res = 0
        if root:
            stack.append((1,root))
        while stack:
            entry = stack.pop()
            res = max(res,entry[0])
            # append left and right if there is
            if entry[1].left:
                stack.append((entry[0] + 1, entry[1].left))
            if entry[1].right:
                stack.append((entry[0] + 1, entry[1].right))
        
        return res

