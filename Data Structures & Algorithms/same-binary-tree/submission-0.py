# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def nodeIsEqual(self, node1, node2):
        return (node1.val == node2.val and node1.left == node2.left and node1.right == node2.right)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue_q = deque()
        queue_p = deque()
        queue_p.append(p)
        queue_q.append(q)

        while queue_q and queue_p:
            nodeP = queue_p.popleft()
            nodeQ = queue_q.popleft()

            if nodeP is not None and nodeQ is not None:
                queue_p.append(nodeP.left)
                queue_q.append(nodeQ.left)
                queue_p.append(nodeP.right)
                queue_q.append(nodeQ.right)
                print(str(len(queue_q)) + " " + str(len(queue_p)))
                if nodeP.val != nodeQ.val:
                    print("hello1 " + str(nodeP.val) + " nodeQ: " + str(nodeQ.val))
                    return False
            elif not (nodeP is None and nodeQ is None):
                print("nodeP " + str(nodeP is not None))
                print("nodeQ " + str(nodeQ is not None))
                return False


        print(str(len(queue_q)) + " " + str(len(queue_p)))
        return True if len(queue_q) == len(queue_p) else False




