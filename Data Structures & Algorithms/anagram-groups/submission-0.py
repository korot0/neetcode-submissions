class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}

        for string in strs:
            chars = [0] * 26

            for char in string:
                index = ord(char) - 97
                chars[index] += 1

            key = tuple(chars)

            if key in words:
                words[key].append(string)
            else:
                words[key] = [string]

        return list(words.values())
        