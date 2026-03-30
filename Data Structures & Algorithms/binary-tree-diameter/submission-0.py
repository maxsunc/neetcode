# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs to traverse thru the tree 
        # how do we keep track of the length?

        # base case at the end
        # if root is None:
        #     return 0
        
        # # recursive case:
        # return max(self.diameterOfBinaryTree(root.left) + 1, self.diameterOfBinaryTree(root.right) + 1)
        # bfs is better since the length could be weird
        queue = deque()
        mostHeight = 0

        queue.append(root)
        while queue:
            node = queue.popleft()
            if node is not None:
                height = self.getHeight(node.left) + self.getHeight(node.right)
                if height > mostHeight:
                    mostHeight = height
                # get the height of both left and right  check if its greater than max
                queue.append(node.left)
                queue.append(node.right)


                # add both left and right to it
        return mostHeight

        # 1: create another function to find the left and right length of a tree
        # traverse the tree and call this function on each guy
        # add th
    def getHeight(self, node) -> int:
        
        if node is None:
            return 0
        # recursive
        # look for the max height guy
        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1
