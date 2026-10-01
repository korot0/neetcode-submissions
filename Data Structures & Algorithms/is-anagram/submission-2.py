class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        new_s = {}
        new_t = {}

        for char in s:
            if char in new_s:
                val = new_s[char] + 1
                new_s[char] = val
            else:
                new_s[char] = 1;

        for char in t:
            if char in new_t:
                val = new_t[char] + 1
                new_t[char] = val
            else:
                new_t[char] = 1;

        return new_s == new_t