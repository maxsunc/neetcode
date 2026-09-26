class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        def sameTree(curNode, curSubRoot):
            # both ended at the same time
            if not curNode and not curSubRoot:
                return True

            # only one ended
            if not curNode or not curSubRoot:
                return False

            return (
                curNode.val == curSubRoot.val
                and sameTree(curNode.left, curSubRoot.left)
                and sameTree(curNode.right, curSubRoot.right)
            )

        if not root:
            return False

        # Try matching starting here
        if sameTree(root, subRoot):
            return True

        # Otherwise search left/right for another starting point
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)