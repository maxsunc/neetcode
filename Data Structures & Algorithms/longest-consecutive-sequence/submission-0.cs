public class Solution {
    public int LongestConsecutive(int[] nums) {
        // 2,20,4,10,3,4,5
        // 2,3,4,4,5,10,20
        if(nums.Length == 0)
            return 0;
        // 
        Array.Sort(nums);

        // O(n + n log(n))

        // order well 
        int highestStreak = 1;
        int currentStreak = 1;
        // 12345 789
        for(int i = 0; i < nums.Length-1; i++){
            if(nums[i] + 1 == nums[i+1] ){
                currentStreak++;
            }
            else if(!(nums[i] == nums[i+1])){
                currentStreak = 1;
            }
            // replace highest
            highestStreak = (currentStreak >= highestStreak) ? currentStreak : highestStreak;
        }

        return highestStreak;

    }
}
