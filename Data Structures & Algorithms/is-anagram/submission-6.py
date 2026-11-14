class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        first = defaultdict(int)
        second = defaultdict(int)

        for i in range(len(s)):
            first[s[i]] += 1
            second[t[i]] += 1

        return first == second
