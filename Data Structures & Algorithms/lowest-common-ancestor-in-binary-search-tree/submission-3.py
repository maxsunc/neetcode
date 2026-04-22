# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # lowest common ancestor
        # not a binary search tree but rather a binary tree??????
        # are they all unique?
        # lowest node that has p and q as descendents ( they can be descendents of themselves)
        
        # in a bst we could've used the bst property that everything on right is bigger than us
        # and everything smaller than us is on the left
        # so we just found the node where the val was in between them

        # the only thing the values are used for are identifying each node as what it is

        # we only care whether the values are in the left subtree or in the right subtree or they are us
        # if those values are there that means this node is a ancestor

        # we call that on every single node

        # that would result in a O(N^2) since its checking each subtree for every node which is slow

        # could check the other subtrees as we're checking other subtrees as well
        result = (None,-1)
        def dfs(curNode, level): # will return [bool, bool] whether p was in the subtree and q in the subtree
            
            if not curNode:
                return [False,False]
            
            # save the result of our boolean pair
            pair = [False,False]

            # check whether we cover any values (current node)
            if curNode.val == p.val:
                pair[0] = True
            elif curNode.val == q.val:
                pair[1] = True

            # check whether left tree covers anything
            left = dfs(curNode.left, level+1)
            
            # check whether right tree covers anything
            right = dfs(curNode.right, level+1)
            pair = [pair[0] or left[0] or right[0], pair[1] or left[1] or right[1]]
            # print(pair)
            
            # if it's all true then update the result
            if pair[0] and pair[1]:
                nonlocal result
                # print(f"setting the result to {curNode.val}")
                result = (curNode,level) if level > result[1] else result

            # return the pair
            return pair
        dfs(root,0)
        return result[0]