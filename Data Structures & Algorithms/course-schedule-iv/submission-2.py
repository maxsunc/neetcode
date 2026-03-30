class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # [a,b] must take course [1] before course B
        # prereqs are indirect not combined
        # instead of and its or now

        # directed graph so our adj list is only one direction
        # to take this course take these prereqs
        adj = defaultdict(list)
        for n1, n2 in prerequisites:
            adj[n2].append(n1) # must take n1 before n2


        # for each of hte query [u,v] we want to check whether u is prereq to v
        # start at v and see if we can get to u or in other words u is a prereq to v, if everything is
        # if there is a loop when we try to visit this node then return False
        visited = set()
        def dfs(course): # return False for cycle
            visited.add(course)
            for prereq in adj[course]:
                if prereq in visited:
                    continue
                if not dfs(prereq):
                    return False
            return True
        answer = []
        # return answers to the queries on whether for [u,v] whether u is prereq to v
        for q1,q2 in queries:
            dfs(q2)
            # dfs returned True lets see if its in the visited set
            verdict = True if q1 in visited else False
            answer.append(verdict)
            visited.clear()
        return answer


