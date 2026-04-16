# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # brute force get the height of left and right and subtract them, repeat for each node
        # this is O(n^2) too slow

        # precompute the height of each node
        balanced = True
        def dfs(node):
            nonlocal balanced
            if not node:
                return 0
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            print(f"for {node.val} left height: {leftHeight}, right height: {rightHeight}")
            if abs(rightHeight - leftHeight) > 1:
                balanced = False
            # return the height of this tree
            return max(leftHeight,rightHeight) + 1
        dfs(root)
        return balanced
                
