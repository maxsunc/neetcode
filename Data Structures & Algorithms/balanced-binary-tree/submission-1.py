# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs
        # brute force: traverse the binary tree
        # find the height of left and right compare them
        # height > 1 ==> return false, else return true
        # O(n^2), space: O(h) where h is the height of the tree
        self.balanced = True
        def dfs(node):
            if node is None:
                return 0
            h1 = dfs(node.left)
            h2 = dfs(node.right)
            print("printing heights")
            print(h1)
            print(h2)
            # check if the heights differ by more than 1
            if self.balanced:
                self.balanced = (abs(h1-h2) <= 1)
            

            return max(h2,h1) + 1
        dfs(root)
        return self.balanced