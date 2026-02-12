class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Map to store the last seen index of each character
        char_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If the character is in our current window, jump 'left' forward
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
            
            # Update the character's last position
            char_map[s[right]] = right
            
            # Calculate length: right index minus left index + 1
            max_length = max(max_length, right - left + 1)
            
        return max_length