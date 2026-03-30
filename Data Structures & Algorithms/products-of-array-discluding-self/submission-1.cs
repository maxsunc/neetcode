

public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int numZeros = 0;
        int productNoZeros = 1;
        List<int> zeroPositions = new List<int>();
        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] == 0)
            {
                numZeros++;
                zeroPositions.Add(i);
                continue;
            }
            productNoZeros *= nums[i];
        }
        int[] result = new int[nums.Length];
        switch (numZeros)
        {
            case 1:
                for (int i = 0; i < nums.Length; i++)
                {
                    if (i == zeroPositions[0])
                    {
                        result[i] = productNoZeros;
                    }
                }
                break;
            case 0:
                for (int i = 0; i < nums.Length; i++)
                {
                    result[i] = productNoZeros / nums[i];
                }
                break;
        }
        return result;
    }
}
