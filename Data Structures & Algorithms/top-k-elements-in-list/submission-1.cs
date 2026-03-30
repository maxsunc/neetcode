

public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        // Step 1: Count frequencies
        Dictionary<int, int> freqMap = new Dictionary<int, int>();
        foreach (int num in nums) {
            if (!freqMap.ContainsKey(num))
                freqMap[num] = 0;
            freqMap[num]++;
        }

        // Step 2: Create buckets where index = frequency
        List<int>[] buckets = new List<int>[nums.Length + 1];
        foreach (var pair in freqMap) {
            int freq = pair.Value;
            if (buckets[freq] == null)
                buckets[freq] = new List<int>();
            buckets[freq].Add(pair.Key);
        }

        // Step 3: Gather top k elements from the buckets (starting from high freq)
        List<int> result = new List<int>();
        for (int i = buckets.Length - 1; i >= 0 && result.Count < k; i--) {
            if (buckets[i] != null) {
                result.AddRange(buckets[i]);
            }
        }

        return result.GetRange(0, k).ToArray();
    }
}
