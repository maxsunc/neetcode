class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # find the ordering of courses to finish all courses
        # if its not possible return an empty array

        # array of prerequisites [a,b] --> must be b to take a, b is a prereq to a
        
        # create an adj list: a : b,c

        # Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]
        # 0 : 1
        # 1 : 2
        # 2 : 0

        # topological sort

        # dfs: look at a course and see if it isn't taken yet then call dfs onto it
        # to take this course, what do I need to take?

        # have a dfs function: if there is a cycle detected then return False
        # if we're able to take this course then return True

        # build our adj list helps us perform dfs
        adjList = defaultdict(set)

        for prereq in prerequisites:
            adjList[prereq[0]].add(prereq[1])

        taken = set()
        seen = set() # clear this each fs root call we make, tracks for cycles
        # taken courses can be kept track by deleting the prereqs of a course 
        res = []

        def dfsCanTake(course):
            if course in seen:
                return False
            # atttempting to take this course
            seen.add(course)
            # check if there are any prereqs still required to take
            for prereq in adjList[course]:
                if prereq not in taken:
                    # check if we can't take it then ret false
                    if not dfsCanTake(prereq):
                        return False
            taken.add(course) # take the course
            res.append(course)
            return True
        
        for i in range(0, numCourses):
            if i not in taken:
                # try to take the course
                if not dfsCanTake(i):
                    return []
                seen.clear()
        return res

        