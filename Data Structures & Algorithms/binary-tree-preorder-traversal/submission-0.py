# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(curNode):
            if not curNode:
                return
            res.append(curNode.val)
            preorder(curNode.left)
            preorder(curNode.right)
        preorder(root)
        return res