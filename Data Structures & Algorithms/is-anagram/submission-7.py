class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_length = len(s)
        if s_length != len(t): return False

        count_s = defaultdict(int)
        count_t = defaultdict(int)

        for i in range(s_length):
            count_s[s[i]] += 1
            count_t[t[i]] += 1

        return count_s == count_t

