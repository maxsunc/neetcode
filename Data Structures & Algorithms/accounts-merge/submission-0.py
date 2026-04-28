class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # accounts[i] = list of strings
        # if there is a common email to both accounts then they are the same

        # [["John","johnsmith@mail.com","john_newyork@mail.com"],["Cane","johnsmith@mail.com","john00@mail.com"],

        # when merging we need to add the emails that are not in the current setup
        # ["John" : set() --> "emails"] # assuming there wont be accounts with different name and matching emails

        # keep a dictionary with string : array of sets()
        # 


        # ["john" : "johnsmith@mail.com"]
        # ["john" : "johnsmith@foo.com"]
        # ["john" : "johnsmith@foo.com", "johnsmith@mail.com"]
        # after merging we need to check whether the current set can merge with any other johns as well
        map = defaultdict(list)

        def checkAndMerge(name,arr):
            sets = map[name]
                # iterate thru arr and check whether they are in sets, if they are in one of them, merge it fully then we'll have to check for merges with that set on the other cases
            merged = False
            for s in sets:
                for i in arr:
                    if i in s:
                        # merge the thing fully iwth this set
                        for i in arr:
                            s.add(i)
                        merged = True
                        # remove the set s:
                        map[name].remove(s)
                        # check for merges with this new set on the other elements
                        checkAndMerge(name,list(s))
                        break
            if not merged:
                map[name].append(set(arr))

        
        for account in accounts:
            name,arr = account[0],account[1::]
            # check wehther the name exists or not
            if name not in map:
                # add as a new entry
                map[name].append(set(arr))
            else:
                checkAndMerge(name,arr)
        res = []
        print(map)
        # convert the map in to an output 
        for key in map:
            for s in map[key]:
                arr = list(s)
                arr.sort()
                entry = []
                entry.append(key) # name
                for st in arr:
                    entry.append(st)
                res.append(entry)
        return res


