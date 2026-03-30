# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # return a 2d array
        # first array has elements at top
        # 2nd array has elements at next level

        # bfs

        # [[1], [2,3], [4,5,6,7]]

        # how do we determine the depth level of each value?
        # use a tuple, starting value at 0 (root node)
        # everytime we add an element from left or right, + 1 to level (index)

        # 
        res = []
        queue = deque()
        if root:
            entry = (0, root)
            queue.append(entry)

        while queue:
            # dequeue the first element of the queue
            front = queue.popleft()

            index = front[0]
            # increase size of reze based on nextIndex
            if len(res) <= index:
                res.append([])
            # add the current value onto result
            res[index].append(front[1].val)

            nextIndex = index + 1

            # add the left and right of that value to the queue
            if front[1].left:
                entry = (nextIndex, front[1].left)
                queue.append(entry)
            if front[1].right:
                entry = (nextIndex, front[1].right)
                queue.append(entry)
        return res
            

