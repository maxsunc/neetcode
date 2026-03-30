class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adjList = defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        # print(adjList)
        # 3. check ffor cycles now
        # perform dfso n every single node
        visited = set()
        
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for nextNode in adjList[node]:
                if nextNode == prev:
                    continue # skip the place we came from
                if not dfs(nextNode, node):
                    return False
            
            return True
        if not dfs(0, -1):
            return False
        return True if len(visited) == n else False

