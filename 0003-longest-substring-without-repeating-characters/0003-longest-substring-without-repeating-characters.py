class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize variables
        max_length = 0  # Length of the longest substring without repeating characters
        start = 0  # Start index of the current substring

        # Dictionary to store the last seen index of each character
        char_map = {}

        # Iterate through the string
        for end in range(len(s)):
            # Check if the current character is already in the substring
            if s[end] in char_map:
                # Update the start index of the substring to the next index after the last occurrence of the current character
                start = max(start, char_map[s[end]] + 1)

            # Update the last seen index of the current character
            char_map[s[end]] = end

            # Update the maximum length if necessary
            max_length = max(max_length, end - start + 1)

        return max_length
