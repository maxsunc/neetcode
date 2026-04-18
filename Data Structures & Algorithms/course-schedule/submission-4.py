class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [0,1] => 1 is prereq to 0
        # there are 0 to numCourses - 1 needed to take


        # we want to see if its possible to finish all courses?

        # just try to prove its false

        # when is it impossible finish all courses
        # interdepencides on each other: 

        # [0,1]
        # [1,0]
        # cycle detection: dfs algorithm is detect a cycle
        # build an adjacency list to traverse the value

        # to catch a cycle we need to explore every single node 

        # clear the seen set each time

        # directed graph => 
        # prereqs of each ccharacter
        adjList = [[] for i in range(0, numCourses)]

        # fill in the adjacency list using prerequisites
        for p in prerequisites:
            i,val = p[0],p[1]
            adjList[i].append(val)
        # [[1,4],[2,4],[3,1],[3,2]]
        # 0 : []
        # 1 : [4]
        # 2 : [4]
        # 3 : [1,2]
        # 4 : []
        seen = set()
        # 2. call dfs on each course from 0 to numCOurses checking for already seen courses
        def dfsCanTake(i):
            if i in seen:
                # this is a cycle detected
                return False
            seen.add(i)

            # check whether we can take prerequisites of this course (if we can then we retunr true)
            pre = adjList[i]
            for val in pre:
                if not dfsCanTake(val):
                    return False # we found a cycle
            seen.remove(i)
            return True
        
        for i in range(numCourses):
            if not dfsCanTake(i):
                return False
            # print(f"good for {i}")
            # seen.clear()

        return True
        
