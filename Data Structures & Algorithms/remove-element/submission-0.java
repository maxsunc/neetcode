class Solution {
    public int removeElement(int[] nums, int val) {
        // find the problematic nodes
        ArrayList<Integer> gi = new ArrayList<Integer>();
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != val){
                // add the problematic index
                gi.add(i);
            }
        }

        for(int i = 0; i < gi.size(); i++){
            nums[i] = nums[gi.get(i)];
        }

        return gi.size();


    
        
    }
}