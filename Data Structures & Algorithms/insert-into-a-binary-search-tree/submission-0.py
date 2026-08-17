# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # i this greater than the value? Go right
        # is this less tha nthe value go left

        # go right: if right doesn't exist make the node equal to a new node with val
        
        if not root:
            return TreeNode(val)
        
        def insert(curNode):
            # assume curNode.val exists
            if val > curNode.val:
                # go right
                if curNode.right:
                    insert(curNode.right)
                else:
                    # insert it directly and we're done
                    curNode.right = TreeNode(val)
            else:
                if curNode.left:
                    insert(curNode.left)
                else:
                    curNode.left = TreeNode(val)
        insert(root)
        return root


