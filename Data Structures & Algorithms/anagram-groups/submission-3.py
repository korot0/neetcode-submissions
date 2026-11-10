class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            char_count = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                char_count[i] += 1
            anagrams.setdefault(tuple(char_count), []).append(s)
        return list(anagrams.values())