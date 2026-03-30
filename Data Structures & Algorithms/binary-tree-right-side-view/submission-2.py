# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # when we get t onull we're done

        # perform dfs

        # go right when possible
        # other wise go right

        # if both null stop
        res = []

        def dfs(node, level):
            if level == len(res):
                res.append(node.val)
            if node.right:
                # go t othe right\
                dfs(node.right, level + 1)
            if node.left:
                # go to left
                dfs(node.left, level + 1)
            else:
                # both null, we're finished
                return

        # level can be represented by the size of our res
        if root:
            dfs(root, 0)
        return res