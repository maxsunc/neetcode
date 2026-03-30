class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // map signature → list of anagrams
        Map<String, List<String>> buckets = new HashMap<>();
        
        for (String s : strs) {
            // count letters
            int[] bucket = new int[26];
            for (char c : s.toCharArray()) {
                bucket[c - 'a']++;
            }
            // build a key like "#1#0#0#2#…"
            String key = "";
            for (int cnt : bucket) {
                System.out.println("Brokie :"  + cnt);
                key = key.concat("?" + String.valueOf(cnt));
            }
            System.out.println(key);
            if(buckets.containsKey(key)){
                // add to the bukcet
                List<String> newGuy = buckets.get(key);
                newGuy.add(s);
                buckets.replace(key, newGuy);
            }
            else{
                // its new
                ArrayList<String> newGuy = new ArrayList<>();
                newGuy.add(s);

                buckets.put(key, newGuy);
            }
        }
        
        // all the grouped anagrams
        return new ArrayList<>(buckets.values());
    }
}
