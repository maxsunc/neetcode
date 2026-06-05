class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 1. create adj list
        adjList = defaultdict(list)

        wordList.append(beginWord)
        for i,word in enumerate(wordList):
            for j in range(0,len(word)):
                pattern = word[:j] + "*" + word[j + 1::]
                adjList[pattern].append(word)
        # ["bat","bag","sag","dag","dot"]
        # "bat" : ["bag"]
        # 2. bfs to find the result
        seen = set() # seen words
        queue = deque()
        seen.add(beginWord) # add the begin word since thats where we're starting from)
        # add all words one off from start
        queue.append((beginWord,1))
        # print(f"{queue}")
        while queue:
            # pop off
            entry = queue.popleft()
            word,transforms = entry[0],entry[1]
            if word == endWord:
                return transforms
            # check the adjacent values
            # create patterns
            for i in range(0,len(word)):
                pattern = word[:i] + "*" + word[i+1::]
                for s in adjList.get(pattern,[]):
                    if s not in seen:
                        seen.add(s)
                        queue.append((s,transforms + 1))
        
        


        return 0



