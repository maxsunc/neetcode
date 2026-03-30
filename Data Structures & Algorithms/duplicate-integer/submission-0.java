class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> bucket = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length; i++){
            if(bucket.get(nums[i]) == null){
                
                // add it to the hashmap
                bucket.put(nums[i], 1);
            }
            else{
                // some guy came before us
                return true;
            }



        }

        return false;
    }
}
