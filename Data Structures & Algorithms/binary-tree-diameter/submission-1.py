# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxDiamter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def getHeightAndDiameter(node) -> int:
            if node is None:
                return 0
            # recursive
            # calculate diameter while traversing the tree

            # look for the max height guy
            height1 = getHeightAndDiameter(node.right)
            height2 = getHeightAndDiameter(node.left)
            if (height1+height2  > self.maxDiamter):
                print("ooga")
                self.maxDiamter = height1 + height2 
            
            return max(height1, height2) + 1
        getHeightAndDiameter(root)
        return self.maxDiamter
        
