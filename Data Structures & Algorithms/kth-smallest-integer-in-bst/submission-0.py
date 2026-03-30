# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # smallest is located all the way to the left 

        # starting from the smallest relement lets see


        # traversal technique that puts it already in sorted order
        # this is called in-order traversal
        # go all the way to the left

        # add value to array

        # go all the way to the right
        sortedArr = []
        def inOrder(curNode):
            if not curNode:
                return
            inOrder(curNode.left)
            sortedArr.append(curNode.val)
            inOrder(curNode.right)
        inOrder(root)

        return sortedArr[k-1]

         