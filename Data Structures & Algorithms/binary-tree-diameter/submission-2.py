# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # look for the longest path between 2 nodes

        # O(n^2) solution: For each of the nodes seen do dfs to seee how long their path can be
        # diameter = maximum of the hieght between left vs right 

        def getHeight(node):
            if not node:
                return 0
            return max(getHeight(node.left), getHeight(node.right)) + 1
        
        def getDiameter(node):
            # get the height of left and right and combine together
            return getHeight(node.left) + getHeight(node.right)
        res = 0
        # foreach get the diameter

        stack = []
        
        if root:
            stack.append((getDiameter(root),root))
        while stack:
            entry = stack.pop()
            res = max(res, entry[0])

            if entry[1].left:
                newEntry = (getDiameter(entry[1].left), entry[1].left)
                stack.append(newEntry)
            if entry[1].right:
                newEntry = (getDiameter(entry[1].right), entry[1].right)
                stack.append(newEntry)
        
        return res



        # O(n) can we sacrifice some space to bring it down to O(n)