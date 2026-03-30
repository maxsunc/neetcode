class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        // two arrays of length 26 (# of characters in the alphabet)
        int bucket1[] = new int[26];
        int bucket2[] = new int[26];

        // fill up the bucket for each guy
        for(int i = 0; i < s.length(); i++){
            // 'b' - 'a' = 1 ASCII
            bucket1[s.charAt(i) - 'a']++;
            bucket2[t.charAt(i) - 'a']++;
        }

        // the two buckets MUST be the same
        for(int i = 0; i < bucket1.length; i++){
            if(bucket1[i] != bucket2[i]){
                return false;
            }
        }
        return true;

    }
}
