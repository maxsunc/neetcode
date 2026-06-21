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
                print(f"cycle detected in {seen} with {course}")
                return False
            seen.add(course)
            # atttempting to take this course
            
            # check if there are any prereqs still required to take
            for prereq in adjList[course]:
                if not dfsCanTake(prereq):
                    return False
            if course not in taken:
                res.append(course)
            taken.add(course)
            seen.remove(course)
            # 0 : []
            # 1 : [0]
            # 2 : []
            return True
        
        for i in range(0, numCourses):
            if i not in taken:
                # try to take the course
                if not dfsCanTake(i):
                    return []
                seen.clear()
        return res

        