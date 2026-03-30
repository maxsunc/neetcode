class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # track frequency of each character
        max_freq = 0  # track the most frequent character
        left = 0     # left pointer of window
        result = 0   # max length so far
        
        for right in range(len(s)):
            # Update frequency count
            count[s[right]] = count.get(s[right], 0) + 1
            # Update max frequency
            max_freq = max(max_freq, count[s[right]])
            
            # If window is invalid (too many replacements needed)
            # window size - max frequency = number of replacements needed
            if (right - left + 1) - max_freq > k:
                # Shrink window
                count[s[left]] -= 1
                left += 1
                
            # Update result with current window size
            result = max(result, right - left + 1)
        
        return result





