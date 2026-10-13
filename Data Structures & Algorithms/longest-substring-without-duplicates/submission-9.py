class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        seen = {}

        for right in range(len(s)):
            char = s[right]
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            seen[char] = right
            longest = max(longest, right - left + 1)
    
        return longest

# We set up the window by starting at 0 expanding right until
# we find a duplicate. Along the way we store the char and its
# index on a hash table. 
# If we find a duplicate, we can "shrink" the window from the
# left. We do this by getting the last seen index of the respective
# char, then we increase it by 1
# Each iteration we update the seen index of a char and calcualte
# the longest.
