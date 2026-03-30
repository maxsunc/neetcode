class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 0 - (numCourses-1)
        # prerequisites = [[1,0]]

        # [0,1]
        reqList = collections.defaultdict(set)
        path = set()
        result = []
        added = set()

        for prereq in prerequisites:
            reqList[prereq[0]].add(prereq[1])
            # 1 --> 0
        # fill in the gaps of numCourses
        for i in range(0,numCourses):
            if i not in reqList:
                reqList[i] = set()
        def checkNotExists(node):
            if node not in added:
                added.add(node)
                return True
            return False

        def dfs(node):
            if node in path:
                # we're in a cycle
                return False
            # no problems with taking this course (no prereqs)
            if len(reqList[node]) == 0:
                if checkNotExists(node):
                    result.append(node)
                return True
            
            # recursive case
            # it is a unvisited value with prereqs
            # mark it as visited
            path.add(node)
            # check if we can take the prereqs
            # iterate through the prereqs
            for prereq in reqList[node]:
                # call dfs on each prereq
                # in the case it returns false that means it doesn't work
                if  not dfs(prereq):
                    return False
            # all the prereqs return true which means we can take them..
            # therefore we can take this course too
            # reset our prereqs
            # we've already proved that this course can be taken
            reqList[node] = []
            # since we're calling dfs on everything, we need to reset this
            path.remove(node)
            #
            if checkNotExists(node):
                result.append(node)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return result


