public class Solution {
    public int LongestConsecutive(int[] nums) {
        if(nums.Length == 0){
            return 0;
        }
        var numbers = new HashSet<int>(nums);

        // foreach(int n in nums){
        //     numbers.Add(n);
        // }

        // 2,20,4,10,3,4,5
        // set{2,20,4,10,3,5}
        int highest = 1;
        foreach(int n in numbers){
            // check for starting
            if(!numbers.Contains(n-1)){
                // 2,3,4,5
                // 10
                // 20

                int currentSequence = 1;
                // go as far as the sequence
                int currentNumber = n+1;
                while(numbers.Contains(currentNumber)){
                    currentSequence++;
                    currentNumber++;
                }

                highest = (highest >= currentSequence) ? highest : currentSequence;
            }
        }

        return highest;


        

        // return highestStreak;



    }
}
