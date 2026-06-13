class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        // change both to a hashmap with occurances and check each
        var sMap : MutableMap<Char, Int> = mutableMapOf()
        var tMap : MutableMap<Char, Int> = mutableMapOf()
        if (s.count() != t.count()){
            return false
        }

        for (c in s){
            sMap[c] = sMap.getOrDefault(c,0) + 1
        }

        for (c in t){
            tMap[c] = tMap.getOrDefault(c,0) + 1
        }

        // check if they match
        for (key in tMap.keys){
            if (tMap[key] != sMap[key]){
                return false
            }
        }
        

        return true

    }
}
