class Solution:
    def jump(self, nums: List[int]) -> int:
        # If the list is empty or only has one item, you're already at the end.
        if len(nums) <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        furthest_reach = 0
        
        # We walk through the array (except for the last element)
        for i in range(len(nums) - 1):
            # Update the furthest point we can possibly reach from here
            furthest_reach = max(furthest_reach, i + nums[i])
            
            # If we've reached the end of the current jump's range...
            if i == current_end:
                jumps += 1            # We must jump
                current_end = furthest_reach  # Our new "limit" is the furthest we found
                
        return jumps