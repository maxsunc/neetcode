class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # the endWord must exist within wordList

        # cat --> "sag"

        # O(26 * n^2) to build the adj list kind of slow but it is what it is
        # cat : bat
        # bat : bag
        # bag : dag
        # sag  (Omitted)
        # dag : sag
        # dot : 
        # 1: Build adjacency list of each letter's connections
        wordList.append(beginWord)
        adj = defaultdict(list)

        def oneCharDiff(str1, str2):
            diff = 0
            for i in range(0, len(str1)):
                if str1[i] != str2[i]:
                    diff += 1
            return diff == 1


        for i in range(0, len(wordList)):
            str1 = wordList[i]
            for j in range(0, len(wordList)):
                if i == j:
                    continue # no self loops
                str2 = wordList[j]
                # check if it is only one letter diff
                if oneCharDiff(str1, str2):
                    adj[str1].append(str2)
        # early return if endWord doesnt exist in their
        print(adj)
        if not endWord in adj:
            print("wtf")
            return 0
        res = len(wordList)
        # use BFS so no cycles stuck
        queue = deque()
        queue.append((beginWord, 1)) # word, timestamp
        while queue:
            entry = queue.popleft()
            word = entry[0]
            timestamp = entry[1]
            # print(f"cjecking: {word}")
            if word == endWord:
                # reached the goal
                res = min(res, timestamp)
                continue
            # check if a timestamp is bigger than the length of wordList then we're in a cycle for too long
            if len(wordList) < timestamp:
                print(f"cycle detected timestamp {timestamp}")
                break
            # explore all posibilities
            for s in adj[word]:
                # explore it
                newEntry = (s, timestamp + 1)
                # print("adding")
                queue.append(newEntry)



        return res if res != len(wordList) else 0
        # probably do bfs insteado f dfs so we dont get stuck on cycles
        # 2: perform bfs starting from startWord to try to get to endWord, if it doesn't work after 
        # n (number of words) iterations return out and retrn -1

        # cat, cag
        # cat : cag
        # cag: cat