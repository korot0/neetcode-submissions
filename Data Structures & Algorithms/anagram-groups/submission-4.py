class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        res = []

        for str in strs:
            key = [0] * 26
            for c in str:
                key[ord(c) - ord('a')] += 1
            if tuple(key) in anagrams:
                anagrams[tuple(key)].append(str)
            else:
                anagrams[tuple(key)] = [str]
            
        for x in anagrams.values():
            res.append(x)

        return res
