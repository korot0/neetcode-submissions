class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        first = defaultdict(int)
        second = defaultdict(int)

        for c in s:
            first[c] += 1

        for c in t:
            second[c] += 1

        return first == second
