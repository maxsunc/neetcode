class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = [[] for i in range(0, numCourses)]

        # build the adj list as our legend
        for prereq in prerequisites:
            # prepreq[1] is the preq to prereq[0]
            prereqs[prereq[0]].append(prereq[1])
        
        # if there is a cycle it is false
        # but if there isnt then we're chillin
        path = set() # use to check for a cycle or not

        def canWeTakeDfs(course):
            # base cases
            # if theres no prereqs we're able to take this course
            if len(prereqs[course]) == 0:
                return True 
            if course in path:
                # we've encountered a loop
                return False
            path.add(course)
            # we know there are prereqs to this
            # can we take the prereqs courses? if we can then we can take this course
            reqs = prereqs[course]
            for req in reqs:
                if not canWeTakeDfs(req):
                    return False
            # clear the prereqs here
            prereqs[course].clear()
            return True

            # foreach of the prereqs call dfs on it and add to path
        
        # call dfs on each course 
        for i in range(0, numCourses):
            if not canWeTakeDfs(i):
                return False
        
        return True

        



