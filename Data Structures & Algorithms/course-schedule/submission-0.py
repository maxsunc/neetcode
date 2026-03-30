class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build our adjacency list
        adjList = collections.defaultdict(set) # <int, prereqList>
        # the path our dfs follows
        path = set()
        for prereq in prerequisites:
            # [0,1]
            adjList[prereq[0]].add(prereq[1])
        # fill in values that dont exist
        for i in range(0,numCourses):
            if i not in adjList:
                adjList[i] = set()
        
        
        # perform dfs onto the adjList
        def dfs(val):
            # base case
            if len(adjList[val]) == 0:
                # reached a free node wow
                return True
            # detect cycle
            if val in path:
                # we made a full cycle
                return False
            path.add(val)
            
            # recursive case
            # move to the child nodes
            prereqs = adjList[val]
            for i in prereqs:
                if not dfs(i):
                    return False
            path.remove(val)
            adjList[val] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True

