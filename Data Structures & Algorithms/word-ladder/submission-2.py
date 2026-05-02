class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # beginWord and endWOrd
        # list of words wordList
        # transform beginWord into endWord
        # can transfrom beginWord to any word within wordList as long as exactly one position is different

        # will their


        # bfs algorithm
        # to end early when we find it
        # we can only jump around in the same vicinity
        # create an adj list: for each character in wordList note the characters it can jump to

        # keep track of seen set for prev seen words so that way we dont take duplicates
        # 1. create adj list
        adjList = defaultdict(list)
        def oneCharDiff(str1, str2):
            if len(str1) != len(str2):
                return False
            differences = 0
            for i,c in enumerate(str1):
                if str1[i] != str2[i]:
                    differences += 1
            return differences == 1

        wordList.append(beginWord)
        for i,word in enumerate(wordList):
            # iterate again and check if their is a one char diff
            for j,word2 in enumerate(wordList):
                if i == j:
                    continue # skip itself
                if oneCharDiff(word,word2):
                    adjList[word].append(word2)
        # ["bat","bag","sag","dag","dot"]
        # "bat" : ["bag"]
        # 2. bfs to find the result
        seen = set() # seen words
        queue = deque()
        seen.add(beginWord) # add the begin word since thats where we're starting from)
        # add all words one off from start
        for word in adjList[beginWord]:
            queue.append((word,2))
            seen.add(word)
        print(f"{queue}")
        while queue:
            # pop off
            entry = queue.popleft()
            word,transforms = entry[0],entry[1]
            if word == endWord:
                return transforms
            # check the adjacent values
            for s in adjList[word]:
                if s not in seen:
                    seen.add(s)
                    queue.append((s,transforms + 1))
        
        


        return 0



