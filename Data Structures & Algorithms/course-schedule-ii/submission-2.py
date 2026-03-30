class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # return the valid courses to take

        # if its impossible return []
        prereqs = defaultdict(list)

        for prereq in prerequisites:
            prereqs[prereq[0]].append(prereq[1])

        result = []
        seen = set()
        path = set()
        def addToRes(course):
            if not course in seen:
                seen.add(course)
                result.append(course)

        def canTakeCourse(course):
            if len(prereqs[course]) == 0:
                # we can take it!
                addToRes(course)
                return True
            # check for a cycle
            if course in path:
                return False
            
            # visit this node
            path.add(course)

            # this node has prereqs: to determine if we can take this we need to see if we can take the prereqs
            for prereq in prereqs[course]: #
                if not canTakeCourse(prereq):
                    return False
            # we can take the course hurray
            addToRes(course)
            prereqs[course].clear()
            return True
        # call canTakeCourse on each course
        for course in range(0, numCourses):
            if not canTakeCourse(course):
                return []
        return result
            


        # ask if we can take each course, if one course returns False return []
