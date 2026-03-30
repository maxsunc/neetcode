class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # initially it had no cycles

        # initially contains n-1 edges with NO CYCLES
        # aka they were all connected

        # return the right most edge that can be removed

        # no self loops or repeated edges

        # use an adj list to traverse thru 
        # cycle detection
        # the added edge will always make a cycle

        # search for the path of a cycle
        # 
        # there is only going to be one cycle, if there is 2 then thats cook wtf

        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # 1: Search for the nodes in a cycle
        path = set()
        endLoopNode = -1
        startLoopNode = -1
        parent = {}
        timestamp = 0
        # visited = set() # to make this O(v + E)

        def findCycleDfs(node, prev):
            nonlocal timestamp
            nonlocal endLoopNode
            nonlocal startLoopNode
            if node in path:
                endLoopNode = prev # this is the node we ended on
                startLoopNode = node
                return True
            path.add(node)
            # print(f"exploring {node}")
            # print(f"parents : {parent}")
            # track the parent of each value 
            parent[node] = prev

            # check if all other nodes have cycle or not
            for next in adj[node]:
                if next == prev:
                    continue
                if findCycleDfs(next, node):
                    return True
            # visited.add(node)
            return False


        # we're guarunteed there only one cycle then since they're all unique and no self loops
        findCycleDfs(1,-1)
            # print(f'found a cyclke at {endLoopNode}')
        # print("___________________________")
        # print(f"startLoop : {startLoopNode}")
        # print(f"startLoop : {startLoopNode}")

        pathSet = set()
        # backtrack from endLoopNode until we get back to endLoopNode
        pathSet.add(endLoopNode)
        curNode = parent[endLoopNode]
        while True:
            # add and advance
            pathSet.add(curNode)
            if curNode == startLoopNode: # just added the start loop node
                break
            curNode = parent[curNode]
            
        

        # print(f"the pathset is {pathSet}")

        # 2: search for rightmost edges with nodes in the cycle
        for i in range(len(edges)-1, -1, -1):
            edge = edges[i]
            print(f"checking {edge}")
            if edge[0] in pathSet and edge[1] in pathSet:
                return edge
        return (0,0)
