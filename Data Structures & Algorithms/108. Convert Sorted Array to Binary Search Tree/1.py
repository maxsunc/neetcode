# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        # sorted arrray:

        # the root node is the middle node
        # recursive binary search

        # [-10,-3,0,5,9]


        def buildTree(left, right): # returns a tree node
            if left > right:
                return None
            mid = (right + left ) // 2
            curNode = TreeNode(nums[mid])

            curNode.right = buildTree(mid + 1, right)
            curNode.left = buildTree(left, mid - 1)
            return curNode

        return buildTree(0, len(nums) - 1)