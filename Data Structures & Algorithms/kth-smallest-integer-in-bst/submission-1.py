# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # solution 1: Have a heap
        # foreach element found put it into the heap
        # this is O(k * logn + n)
        # doesn't make use of the bst property

        # bst property: left is smaller than us and right is bigger than us

        # build out a sorted ascending array by traversing the bst in order

        # build the array


        # return the index at k - 1
        arr = []
        # 1. build the array out by doing a inorder traversal of bst
        def inOrder(node):
            if not node:
                return
            nonlocal arr
            inOrder(node.left)
            arr.append(node.val)
            inOrder(node.right)
            
        inOrder(root)
        # 2. return the k - 1 index
        return arr[k-1]