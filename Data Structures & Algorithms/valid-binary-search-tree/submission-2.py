
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # left subtree contains nodes less than curNodes key

        # right subtree contains nodes greater than nodes key
        # recursively call onto left and right
        # base case (no children => true)

        def check(curNode, minVal, maxVal):

            # keep track of the max and min value that we've seen descending with dfs
            # when we get to the end we're done
            if not curNode:
                return True
            
            if not (minVal < curNode.val < maxVal):
                return False

            # use the min val for the left side
            # use the max val for right side
            rightWorks = check(curNode.right, curNode.val, maxVal)
            # left size updates the max val
            leftWorks = check(curNode.left, minVal, curNode.val)
            
            return rightWorks and leftWorks
        return check(root, float('-inf'), float('inf'))