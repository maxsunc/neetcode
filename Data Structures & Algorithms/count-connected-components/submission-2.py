class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # find the number of conntected components
        # undirected graph

        # dfs should be able to explore the whole thing

        # probably want to build an adj list to traverse easier
        
        # keep a visited set of nodes we already visited
        # in the dfs if it is visited return 
        
        adj = defaultdict(list)

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        # dfs solution
        visited = set()

        # def dfsVisit(node, prev):
        #     if node in visited:
        #         return
        #     visited.add(node)
        #     # visit all children that arent the prev node visited
        #     for child in adj[node]:
        #         if child == prev:
        #             continue # skip so we dont go back and forth
        #         dfsVisit(child, node)

        # res = 0
        # # call dfs on nodes that aren't visited
        # for i in range(0, n):
        #     if not i in visited:
        #         res += 1
        #         dfsVisit(i,-1)
        res = 0
        # bfs solution:
        # for ech of hte guys not in visited lets call bfs on it
        for i in range(0, n):
            if not i in visited:
                res += 1
                # use bfs to explore the whole thing
                queue = deque()
                entry = (i, -1)
                queue.append(entry)
                while queue:
                    entry = queue.popleft()
                    visited.add(entry[0])
                    prev = entry[1]
                    # explore all nodes connected to entry[0]
                    for node in adj[entry[0]]:
                        if node == prev or node in visited:
                            continue
                        newEntry = (node, entry[0])
                        # add to the queue to explore
                        queue.append(newEntry)


        return res
