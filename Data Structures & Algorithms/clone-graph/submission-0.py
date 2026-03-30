"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        # dfs to traverse the graph
        # how do we traverse an adjacency list?
        # node(4,[Node(3), Node(5),Node(4)])
        # 
        # traver node while making our deep copy
        # keep a hashmap of visited nodes
        # 
        clonedNodes = {} # <int, Node>
        # how do we even go about building our own cloned graph
        
        # dfs will traverse the node and return a result (root node of the copy)
        # Clone fudging takes original node and clones
        def clone(node):
            
            # base case prevents you from cloning already cloned nodes
            if node.val in clonedNodes:
                return clonedNodes[node.val]

            copy = Node(node.val)
            clonedNodes[node.val] = copy # value - new
            # copy all the neighbors and store them into clonedNodes
            # then put those neighbors into copy's neighbor boom
            for c in node.neighbors:

                # clone the neighbor amd put it into copy's neighbors
                copy.neighbors.append(clone(c))
            return copy


            


        result = clone(node)
        return result
            

